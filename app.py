import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2", base_url="http://13.126.61.209/11434")

template = """
Answer the Question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(context, question):
    result = chain.invoke({"context": context, "question": question})
    context += f"\nUser: {question}\nAI: {result}"
    return result, context

st.title("Commudle Chatbot")

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
