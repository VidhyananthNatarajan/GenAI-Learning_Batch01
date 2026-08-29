import streamlit as st

# Page config & setup

st.set_page_config(page_title="Gen AI demo",layout="wide")

st.title("Gen AI demo")

# side bar controls

with st.sidebar:
    st.title("Configuration Controls")
    model_choice = st.selectbox("Model", ["GPT-4.1", "claude-4.6 Sonnet", "LLaMA-3 70B Chat", "Mistral 7B Chat", "Falcon 180B Chat"])
    temperature =st.slider("Temparature",0.0,1.0,0.5)

# state Initialization

if "messages" not in st.session_state:
    st.session_state.messages=[]
