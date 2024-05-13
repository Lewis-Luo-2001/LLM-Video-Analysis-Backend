import os

from fastapi import FastAPI, UploadFile, status, Response, BackgroundTasks

from handler import audio, file
from model.audio_model import AudioModel
from pytube import YouTube
import moviepy.editor

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/youtube")
async def get_youtube_mp3(background_tasks: BackgroundTasks, url: str):

    id = generate(size=15)
    video_path = f"tmp/{id}/temp_video.mp4"
    audio_path = f"tmp/{id}/temp_audio.mp3"

    # Download YouTube video
    youtube = YouTube(url)
    video = youtube.streams.get_lowest_resolution()
    video.download(output_path=f"tmp/{id}", filename="temp_video.mp4")

    # Convert video to mp3
    video = moviepy.editor.VideoFileClip(video_path)
    clip_audio = video.audio
    clip_audio.write_audiofile(audio_path)

    background_tasks.add_task(audio.generate_transcript, audio_path)

    return {
        "id": id
    }

@app.post("/audio", status_code=201)
async def post_audio(up_file: UploadFile, background_tasks: BackgroundTasks):
    # generate the id by hash(filename)
    id = hash.hash(up_file.filename)

    # save the audio file
    audio_path = file.save_audio(up_file, id)

    # generate the transcript with whisper
    background_tasks.add_task(audio.generate_transcript, audio_path)

    return {
        "id": id
    }

@app.get("/transcript/{id}", status_code=200)
def get_transcript(id: str, response: Response):
    dir_path = os.path.join("tmp", id)
    transcript_path = os.path.join("tmp", id, "transcript.txt")
    
    # check if the id exists
    print(dir_path)
    if not os.path.isdir(dir_path):
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    # check if the transcript exists
    if not os.path.isfile(transcript_path):
        response.status_code = status.HTTP_202_ACCEPTED
        return

    with open(transcript_path, 'r') as f:
        transcript = f.read()

    return {
        "transcript" : transcript
    }
    

