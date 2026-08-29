import streamlit as st
import time

st.title("Agent Inspector & Status")

if st.button("Run Agent"):
    with st.status("Agent Intialized...",expanded =True) as status:
        st.write("Agent is running...")
        time.sleep(1)
        st.write("Agent is processing the request...")
        time.sleep(1)
        st.write("Agent is calling the tools...")
        time.sleep(1)
        status.update(label="Agent completed the processing",state="complete",expanded=False)

st.success("Agent has completed the processing successfully!")        
