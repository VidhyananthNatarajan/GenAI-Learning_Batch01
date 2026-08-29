import streamlit as st
import time

st.title("Spinner example")

if st.button("Load Dashboard Data"):
    with st.spinner("Fetching data from API... please wait..."):
        time.sleep(2)

    st.success("Data fetched successfully!")            