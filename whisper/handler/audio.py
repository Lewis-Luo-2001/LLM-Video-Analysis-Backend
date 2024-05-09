import os

import whisper

def generate_transcript(audio_path: str) -> str:
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_path)

    # save the transcript
    directory_path = os.path.dirname(audio_path)
    text_path = os.path.join(directory_path, "transcript.txt")
    with open(text_path, 'w') as f:
        f.write(result["text"])