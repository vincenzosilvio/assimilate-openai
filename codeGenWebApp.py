import streamlit as st
from oalib.solutions import code_generator

st.title("👨‍💻 AI Code Generator")
st.write("Convert a comment into code in any language using GPT-4o-mini model")

language = st.text_input("Programming Language", "Python 3")
text = st.text_area("Comment", "Calculate the mean distance between an array of points")

if st.button("Generate Code"):
    code = code_generator(text, language)
    st.write("```" + language + "\n" + code + "\n```")


