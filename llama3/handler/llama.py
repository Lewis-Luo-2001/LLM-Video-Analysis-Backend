from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

from model import chat_model

def summarize(transcript: str) -> str:
    llm = Ollama(model='llama3')
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a teaching assistant, I will give you transcript of a video. Please summary the information in the video, and also list the key points of the video."),
        ("user", "{input}"),
    ])

    chain = prompt | llm

    return chain.invoke({"input": transcript})

def chat(context: chat_model.Context) -> str:
    llm = Ollama(model='llama3')

    # system prompt
    system_prompt = ChatPromptTemplate.from_messages([
        ("system", "These are transcript of a video and the context of our previous chatting, please answer the question base on the context: " + context.transcript.context),
    ])

    chain = system_prompt

    # history prompt
    chat_history = []

    for chat in context.chatbody:
        chat_history.append((chat.role, chat.content))
        history_prompt = ChatPromptTemplate.from_messages(chat_history)

        chain = history_prompt | llm

    chain = chain | llm

    return chain.invoke({"input": context.question})