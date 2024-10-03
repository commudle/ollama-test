import streamlit as st 
from langchain_community.llms import Ollama 
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model="llama3.2", base_url ="http://13.126.61.209:11434")

st.title("Commudle Chatbot")

template = """
Answer the Question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

#prompt = st.text_area("Enter your prompt:")

# if st.button("Generate"):
#         if prompt:
#             with st.spinner("Generating response..."):
#                 st.write_stream(llm.stream(prompt, stop=['<|eot-id|>']))

def handle_conversation(context, question):
    prompt = f"{context}\nUser: {question}\nAI:"
    result = llm.invoke(prompt)
    context += f"\nUser: {question}\nAI: {result}"
    return result, context

if "context" not in st.session_state:
    st.session_state.context = ""

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        result, updated_context = handle_conversation(st.session_state.context, user_input)
        st.session_state.context = updated_context
        st.write(f"Bot: {result}")

if st.session_state.context:
    st.write("Conversation History:")
    st.text(st.session_state.context)

