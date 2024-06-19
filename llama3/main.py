from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import model.chat_model as model

from handler import llama, gemini

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

@app.post("/task")
def post_subtitle(context: model.Context) :

    if context.model == 'llama3':
        answer = llama.task(context.context, context.language_tag)
    elif context.model == 'gemini':
        answer = gemini.interact_with_gemini(context.context, context.language_tag, is_task=True)

    return {
        "answer": answer,
    }


@app.post("/chat")
def post_subtitle(context: model.Context) :

    if context.model == 'llama3':
        answer = llama.chat(context.context, context.language_tag)
    elif context.model == 'gemini':
        answer = gemini.interact_with_gemini(context.context, context.language_tag)

    return {
        "answer": answer,
    }
