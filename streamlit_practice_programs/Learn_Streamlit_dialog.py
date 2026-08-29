import streamlit as st

# creating a dialog popup function using the decorator
@st.dialog("Confirmation Dialog")
def show_popup():
    st.write("Are you sure you want to proceed this action?")

    if st.button("Yes,Proceed"):
        st.session_state.confirmed = True
        st.rerun()

    if st.button("No,Cancel"):
        st.session_state.confirmed = False
        st.rerun()    

@st.dialog("Confirmation Alert")
def show_popup1():
    st.write("Are you sure you want to proceed?")

    if st.button("Yes,Proceed"):
        st.session_state.confirmed1 = True
        st.rerun()

    if st.button("No,Cancel"):
        st.session_state.confirmed1 = False
        st.rerun()         


# Main Page layout

st.title("Streamlit Dialog Popup Example")

if "confirmed" not in st.session_state:
    st.session_state.confirmed = False

if st.button("Click Dialog"):
        show_popup()

if st.session_state.confirmed:
    st.success("User selected Yes!")   
    st.session_state.confirmed = False  
else:
    st.info("User selected No!")   

if "confirmed1" not in st.session_state:
    st.session_state.confirmed = False    


if st.button("Click Alert"):
         show_popup1()

if st.session_state.confirmed1:
    st.success("User confirmed the action!")   
    st.session_state.confirmed1= False  
else:
    st.info("User rejected the action!")              