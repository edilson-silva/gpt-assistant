import os

from openai import OpenAI
from openai.resources.chat.completions import ChatCompletion

OPENAI_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_KEY)


def get_summary(content: str) -> str:
    """
    get content summary

    Args:
        content (str): content to generate summary

    Returns:
        str: summarized content
    """
    chat_completion: ChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em resumo de textos e que responde em português.",
            },
            {"role": "user", "content": content},
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion["choices"][0]["message"]["content"]


def get_answer(content: str, question: str) -> str:
    """
    get question response based on content

    Args:
        content (str): content to generate summary

    Returns:
        str: answer for user question
    """
    chat_completion: ChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista que sabe responder perguntas com base no texto e que responde em português.",
            },
            {
                "role": "assistant",
                "content": f"Responda as perguntas com base no seguinte texto: {content}",
            },
            {"role": "user", "content": question},
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion["choices"][0]["message"]["content"]
