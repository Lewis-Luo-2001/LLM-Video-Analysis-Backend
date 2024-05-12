import mimetypes
import os

from fastapi import UploadFile

APP_ROOT = '/home/dcslab/LLM-Video-Analysis-Backend/whisper'

def save_audio(file: UploadFile, id: str) -> str:
    # save audio
    extension = mimetypes.guess_extension(file.content_type)

    audio_dir = os.path.join(
        APP_ROOT, 'tmp', id
    )

    audio_path = os.path.join(
        audio_dir, f'audio{extension}'
    )

    if(os.path.isdir(audio_dir)):
        return audio_path

    os.makedirs(audio_dir)

    with open(audio_path, 'wb') as audio_file:
        audio_file.write(file.file.read())

    return audio_path