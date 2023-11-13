from commom import util
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from services import openapi

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check
@app.get("/", response_class=PlainTextResponse)
async def health_check() -> str:
    """
    api health check

    Returns:
        str: a simple message indicating api is running
    """
    return "API alive"


@app.get("/summary", response_class=PlainTextResponse)
async def summary(url: str) -> str:
    """
    get summary from webpage

    Args:
        url (str): webpage url to extract content

    Returns:
        str: summarized content
    """
    content = await util.get_page_content(url)
    summary = openapi.get_summary(content)

    return summary


@app.get("/answer", response_class=PlainTextResponse)
async def answer(url: str, question: str) -> str:
    """
    get answer for a question based on a webpage content

    Args:
        url (str): webpage url to extract content
        question (str): question to be answered

    Returns:
        str: answer for user question
    """
    content = await util.get_page_content(url)
    answer = openapi.get_answer(content, question)

    return answer
