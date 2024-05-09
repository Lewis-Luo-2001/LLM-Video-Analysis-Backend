from fastapi import FastAPI
import model.model as model

import handler.llama as llama

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.post("/transript")
def post_transript(transript: model.Transript):
    summary = llama.summarize(transript.context)

    return {
        "summary": summary
    }

@app.post("/chat")
def post_subtitle(chatbody: model.Chatbody):
    answer = llama.chat(chatbody.question, chatbody.context)
    context = chatbody.context + "question: " + chatbody.question + "\nanswer: " + answer

    return {
        "answer": answer,
        "context": context
    }
