import streamlit as st

st.title("File Upload Example")

uploaded_files= st.file_uploader(label="upload documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"uploaded Files ({len(uploaded_files)})")
    for file in uploaded_files:
        st.write(f"'{file.name}'({file.size}bytes)")
