"""" Library with OpenAI solutions as functions """

import openai   
import os

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