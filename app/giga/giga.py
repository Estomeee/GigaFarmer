from langchain.chains import ConversationalRetrievalChain
from langchain.schema import Document
from langchain.retrievers import BM25Retriever
from langchain.chat_models.gigachat import GigaChat
import json
from razdel import tokenize as tknz
from app.config import GIGA_TOKEN

def get_tokens(s: str) -> list[str]:
    tokens = list(tknz(s))
    return [_.text for _ in tokens]


def get_giga_retriever():
    with open("./app/text.txt", encoding="utf8") as json_file:
        data = json.load(json_file)

    documents = [Document(page_content=content) for content in data]

    bm25_retriever = BM25Retriever.from_documents(
        documents=documents,
        preprocess_func=get_tokens,
        k=3,
    )

    giga = GigaChat(
        verify_ssl_certs=False,
        profanity=False,
        credentials=GIGA_TOKEN,
    )

    return ConversationalRetrievalChain.from_llm(giga, retriever=bm25_retriever)
