from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

def summarize(transcript: str) -> str:
    llm = Ollama(model='llama3')
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a teaching assistant, I will give you transcript of a video. Please summary the information in the video, and also list the key points of the video."),
        ("user", "{input}"),
    ])

    chain = prompt | llm

    return chain.invoke({"input": transcript})

def chat(question: str, context: str) -> str:
    llm = Ollama(model='llama3')
    prompt = ChatPromptTemplate.from_messages([
        ("system", "These are the context of our previous chatting, please answer the question base on the context."),
        ("system", context),
        ("user", "{input}"),
    ])

    chain = prompt | llm

    return chain.invoke({"input": question})