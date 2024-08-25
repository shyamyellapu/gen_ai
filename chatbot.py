import streamlit as st
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

os.environ["LANGCHAIN_KEY"]="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"
prompt=ChatPromptTemplate([
    """
    write about the topic {Topic}.
    """
])
output=StrOutputParser()
llms=Ollama(model="llama2")
chain=prompt|llms|output
st.title("CHATBOT")
topic=st.text_input("Enter topic")
st.write(chain.invoke({"Topic":topic}))
