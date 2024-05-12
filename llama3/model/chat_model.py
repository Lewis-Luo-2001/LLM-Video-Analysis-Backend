from typing import List

from pydantic import BaseModel

class Transcript(BaseModel):
    url: str = None
    context: str

class Chatbody(BaseModel):
    role: str
    content: str

class Context(BaseModel):
    transcript: Transcript
    chatbody: List[Chatbody]
    question: str