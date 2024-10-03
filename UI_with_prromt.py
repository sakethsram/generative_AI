import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project='engaged-reducer-432905-c5', location='asia-east1')
model = GenerativeModel("gemini-1.5-pro-001")

def get_vertexai_response(prompt):
    response = model.generate_content([prompt])
    return response

def streamlit_example():
    st.title("Chat-Bt: WhatsApp's Datascience Group")
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a question:")
    if not prompt:
        return
    
    user_message = {"role": "user", "content": prompt}
    st.session_state["messages"].append(user_message)
    with st.chat_message("user"):
        st.markdown(prompt)
    
    reply = get_vertexai_response(prompt)
    
    assistant_message = {"role": "assistant", "content": reply}
    st.session_state["messages"].append(assistant_message)
    with st.chat_message("assistant"):
        st.markdown(reply)

def main():
    streamlit_example()
    
if __name__ == "__main__":
    main()
