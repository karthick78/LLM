## integrate our code with openai

import os
from constants import openapi_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain


import streamlit as st

os.environ['OPENAI_API_KEY']=openapi_key




# stream let initialize

st.title("Celebrity Search Results")
input_text=st.text_input("search the topic you want")

#PROMPT TEMPLATES

first_input_prompt=PromptTemplate(
	input_variables=['name'],
	template=" Tell me about celebrity {name}"
)



llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True) 
   
if input_text:
	st.write(chain.run(input_text))
	
