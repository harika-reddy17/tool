import streamlit as st
import ollama
st.title("AI chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
         st.markdown(message["content"])
user_input = st.chat_input("Ask me anything!")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )
    bot_response = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)