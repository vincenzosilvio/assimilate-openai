import streamlit as st
import openai
import os

# Get the OpenAI API Key
api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

# Setting up the Title
st.title("🕹️ AI Question Answering Bot")

st.write(
    "_**Intelligent QA bot that will answer all your questions in zero shot based on the context from the internet.**_"
)

QUESTION = st.text_input("Input Question 👇")


@st.cache
def submit_question(text):
    """This submits a question to the OpenAI API"""
    openai.api_key = os.getenv("OPENAI_API_KEY")

    
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Please keep your responses concise"},
            {"role": "user", "content": text},
        ],
    )

    return completion.choices[0].message.content


if st.button("Submit"):
    st.write("**Output**")
    st.write("""---""")
    with st.spinner(text="In progress"):
        report_text = submit_question(QUESTION)
        st.markdown(report_text)
