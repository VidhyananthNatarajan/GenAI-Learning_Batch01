import streamlit as st

st.title("Agent Evaluation - Feedback response")

# Simulated Agent output

st.chat_message("assistant").write("Here is the summary of Q3. Q3 revenue is up by 20% compared to Q2. The main drivers for this growth are increased sales in the North American region and the successful launch of our new product line.")

# Feedback widget
rating =st.feedback(options="thumbs",key ="feedback_summary_Q3")

if rating is not None:
   sentiment = "Positive" if rating ==  1 else "Negative"

   if sentiment =="Positive":  
    st.info("Thank you for your positive feedback! We appreciate your support and are glad to hear that you found the summary helpful." )  

   else:
    st.info("Thank you for your feedback! We value your input and will use it to improve our future summaries. If you have any specific suggestions or concerns, please feel free to share them with us.")   

   st.session_state["feedback"] = sentiment

   st.toast(f"Feedback recorded: {sentiment}")