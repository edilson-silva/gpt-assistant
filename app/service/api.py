import os

import requests
from dotenv import load_dotenv

load_dotenv()


API_URL = os.getenv("API_URL")


def get_summary(url: str) -> str:
    endponint = f"{API_URL}summary"
    response = requests.get(endponint, params={"url": url})

    if response.ok:
        return response.text

    return "Getting data error"


def get_answer(url: str, question: str) -> str:
    endponint = f"{API_URL}answer"
    response = requests.get(endponint, params={"url": url, "question": question})

    if response.ok:
        return response.text

    return "Getting data error"
