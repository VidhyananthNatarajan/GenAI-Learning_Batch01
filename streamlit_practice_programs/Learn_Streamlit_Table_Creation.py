import streamlit as st
import pandas as pd

st.title("Streamlit Table Creation Example")

st.subheader("Retrived Documents")

st.markdown("###$$ Basic Text Addition ####$$")
st.markdown("This is a simple example of how to create a table in Streamlit using the `data_editor` function")

data =pd.DataFrame(
   {
     "Select Context":[False,True,True],  
     "Doc ID":[1,2,3],
     "Name":["Doc 1", "Doc 2", "Doc 3"],
     "Score":[0.95, 0.85, 0.75],
     
  }

)

st.data_editor(data, use_container_width=True)



