# importing the required packages
from openai import OpenAI
import streamlit as st

# reading the openAI api-key
f = open("keys\.openAI_Key.txt")

OPENAI_API_KEY = f.read()

client = OpenAI(api_key=OPENAI_API_KEY)

# streamlit Application header#
st.title("Code Fix")
st.subheader("Fix the errors in your python code in seconds with understanding!")
###############################

# getting prompt from user
prompt = st.text_area("Enter your python code snippet here🐍!")

# Using GPT3.5_turbo-16k for checking and returning response
if st.button("Generate") == True:
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": """check for any errors for the python code snippet provided by the users. If there are any errors, list those errors and give the corrected code snippet.""",
            },
            {"role": "user", "content": prompt},
        ],
    )
    st.write(response.choices[0].message.content)
