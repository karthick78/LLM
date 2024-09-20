## integrate our code with openai

import os
from constants import openapi_key
from langchain.llms import OpenAI
from langchain inport PromptTemplate




import streamlit as st

os.environ['OPENAI_API_KEY']=openapi_key

# stream let initialize

st.title("Lang Chain Demo with OpenAPI")

input_text=st.text_input("search the topic you want")


#PROMPT TEMPLATES

first_input_prompt=PromptTemplate(
	input_variables=['topic']
)

llm=OpenAI(temperature=0.8)

if input_text:
	st.write(llm(input_text))
	
