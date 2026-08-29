import streamlit as st
import time

# title of the app
st.title("My First Streamlit App")

st.write("Hello, Welcome to my first streamlit app!")

st.chat_input("Type your message here...")

# dropdown

st.selectbox("Model",["GPT-4.1","claude-4.6 Sonnet","LLaMA-3 70B Chat","Mistral 7B Chat","Falcon 180B Chat"])

# Message

st.chat_message("user").write("Hello, how are you?")

st.chat_message("assistant").write("Hello, I am AI Assistant. How can I help you?")

# Streaming

def text_generator():
    response = "This is a sample response from the AI assistant. It can be a long text that is streamed in chunks."
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.01)   # brief pause to simulate streaming   

# Trigger the streaming using a button
if st.button("Start Streaming"):
    output = st.write_stream(text_generator())        
