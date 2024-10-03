from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the Question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2")
prompt= ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to commudle chatbot")
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": question})
        print("Bot: ", result)
        context += f"\nUser: {question}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()