import streamlit as st
import time

st.title("Agentic Chatbot")

# 1. Memory Intializtion

if "messages" not in st.session_state:
    st.session_state.messages = [
      {"role":"assistant","content":"Hello! I am your agentic chatbot. How can I assist you today?"}
    ]  

# 2.Render the chat history
for message in st.session_state.messages:    
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Accept user input        
if prompt :=st.chat_input("Type your message here..."):
    # append the user message to the chat history
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
            st.markdown(prompt)


# 4. simulate the Agent Actions

with st.chat_message("assistant"):
     with st.status("Agent starts Thinking & running tools calls...",expanded=True) as status:
          st.write("Searching the Vector DB...")
          time.sleep(1)
          st.write("Calling the tools") 
          time.sleep(1)
          status.update(label="completed the processing",state="complete",expanded=False)

def response_generator():
     response = f"Agent processed the query: '{prompt}'. Here is the output breakdown..."
     for word in response.split(" "):
             yield word + " "
             time.sleep(0.05)   # brief pause to simulate streaming   

full_response = st.write_stream(response_generator())  

# Append & store the response in the Memory
st.session_state.messages.append({"role":"assistant","content":full_response})



