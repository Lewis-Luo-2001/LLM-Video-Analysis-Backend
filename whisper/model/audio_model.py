from fastapi import UploadFile

from pydantic import BaseModel

class AudioModel(BaseModel):
    language_tag: str
    translate_tag: str