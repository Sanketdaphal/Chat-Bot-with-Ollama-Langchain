 

#help to interact with OpenAI's chat models
 
#if want to write prompts in a more convenient way
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
#to manage the response from the model
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

 

##creating charbot
Prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that helps people find information.") ,
    ("user","Question: {question}"),
])


#streamlit framework
st.title("Chatbot with Langchain and Ollama")
st.subheader("sanket's")
st.write("Ask me anything!")
st.selectbox("Select Model", ["gemma3:1b", "gemma2:7b", "llama3:7b", "llama2:13b"])
input_text = st.text_input("search the topic you want")

#openAI llm call

llm = Ollama(model = "gemma3:1b")
output_parser = StrOutputParser()

##chain
chain = Prompt|llm|output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response) 