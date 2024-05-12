from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import model.chat_model as model

from handler import llama

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.post("/transcript")
def post_transript(transcript: model.Transcript):
    summary = llama.summarize(transcript.context)

    return {
        "summary": summary
    }

@app.post("/chat")
def post_subtitle(context: model.Context):
    answer = llama.chat(context)

    # context.chatbody.append({"role": "user", "content": context.question})
    # context.chatbody.append({"role": "assistant", "content": answer})

    return {
        "answer": answer,
        # "transcript": context.transcript,
        # "history": context.chatbody,
    }
