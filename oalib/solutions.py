"""" Library with OpenAI solutions as functions using gpt-4o-mini model 
For reference use https://platform.openai.com/docs/api-reference/introduction """

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


#build a function that converts a comment into code in any language using gpt-4o-mini model
def code_generator(text, language):
    """This generates code from a comment using the OpenAI API.
    
    Example: 
        code = code_generator("# Calculate the mean distance between an array of points", "Python 3")
        print(code)
    
    Args:
        text (str): The comment from which to generate code.
        language (str): The programming language for the code.
        
    Returns:
        str: Generated code.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Format the message with the language and user comment
    formatted_text = f"## {language}\n{text}\n\nPlease generate the code for the above comment."
    print

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes code."},
            {"role": "user", "content": formatted_text},
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    return completion.choices[0].message['content'].strip()

    