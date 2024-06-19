from typing import List

from pydantic import BaseModel

class Transcript(BaseModel):
    url: str = None
    context: str

class Chatbody(BaseModel):
    role: str
    content: str

class Context(BaseModel):
    context: List[Chatbody]
    language_tag: str
    model: str = 'llama3'