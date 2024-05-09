from pydantic import BaseModel

class Transript(BaseModel):
    url: str = None
    context: str

class Chatbody(BaseModel):
    question: str
    context: str