import os
import time

import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from service.api import get_summary

load_dotenv()

SITE_URL = os.getenv("SITE_URL")

SUMMARY_ENDPOINT = "summary"
QUESTION_ENDPOINT = "answer"


col1, col2 = st.columns([0.3, 0.7])

with col1:
    logo = Image.open("public/images/logo.png")
    st.image(logo, width=150)

with col2:
    st.header("Hello!")
    st.header("My name is 3X, your personal assistant")


summary_tab, answer_tab = st.tabs(["summary", "answer"])


def print_response(label: str = "Response", text: str = ""):
    st.columns([1.0])
    st.markdown(f"### {label}:")
    st.markdown("---")

    text_size = len(text) + 1

    t = st.empty()

    for i in range(text_size):
        text_slice = text[0:i]
        t.markdown(f"##### {text_slice}")
        time.sleep(0.05)


with summary_tab:
    url = st.text_input("Type site URL to make a content resume")
    make_summary_button = st.button("Go")

    if make_summary_button:
        summary = get_summary(url)

        print_response("Summary", summary)
