from typing import List


from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


from model import chat_model

def summarize(transcript: str) -> str:
    llm = Ollama(model='llama3', num_ctx=8192)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a teaching assistant, I will give you transcript of a video. Please summary the information in the video, and also list the key points of the video."),
        ("user", "{input}"),
    ])

    chain = prompt | llm

    return chain.invoke({"input": transcript})

def chat(context: List[chat_model.Chatbody], language: str = 'en') -> str:
    # context[0] -> transcript
    # context[-1] -> question

    llm = Ollama(model='llama3', num_ctx=8192)

    embeddings = OllamaEmbeddings()

    vector = FAISS.from_texts([context[0].content], embeddings)
    retriever = vector.as_retriever()

    if language == 'zh' :
        prompt = ChatPromptTemplate.from_messages([
            ('system', '以下請持續使用中文，回答用戶的問題基於以下上下文，上下文是影片的字幕：\n\n{context}'),
            ('user', '{input}'),
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            ('system', 'Answer the user\'s questions based on the below context:\n\n{context}'),
            ('user', '{input}'),
        ])

    document_chain = create_stuff_documents_chain(llm, prompt)

    if language == 'zh':
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "鑒於上述對話，請用繁體中文回答生成一個搜索查詢以獲取與對話相關的信息")
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
        ])

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

    chat_history = []

    for chat in context[1:-1]:
        if chat.role == "user":
            chat_history.append(HumanMessage(content = chat.content))
        if chat.role == "assistant":
            chat_history.append(AIMessage(content = chat.content))

    response = retrieval_chain.invoke({
        'input': context[-1].content,
        'chat_history': chat_history,
    })

    return response['answer']

def task(context: List[chat_model.Chatbody], language: str = 'en') -> str:
    # context[0] -> transcript
    # context[-1] -> question

    llm = Ollama(model='llama3', num_ctx=8192)

    embeddings = OllamaEmbeddings()

    vector = FAISS.from_texts([context[0].content], embeddings)
    retriever = vector.as_retriever()

    if language == 'zh' :
        prompt = ChatPromptTemplate.from_messages([
            ('system', '以下請持續使用中文，回答用戶的問題基於以下上下文，上下文是影片的字幕：\n\n{context}'),
            ('user', '{input}'),
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            ('system', 'Answer the user\'s questions based on the below context, the context is transcript of a video:\n\n{context}'),
            ('user', '{input}'),
        ])

    document_chain = create_stuff_documents_chain(llm, prompt)

    if language == 'zh':
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "鑒於上述對話，請以markdown格式用繁體中文回答生成針對影片內容對於用戶有幫助的內容或是摘要")
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "Given the above conversation, generate a summary of the content of the video that is helpful to the user in Markdown format.")
        ])

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

    chat_history = []

    for chat in context[1:-1]:
        if chat.role == "user":
            chat_history.append(HumanMessage(content = chat.content))
        if chat.role == "assistant":
            chat_history.append(AIMessage(content = chat.content))

    response = retrieval_chain.invoke({
        'input': context[-1].content,
        'chat_history': chat_history,
    })

    return response['answer']