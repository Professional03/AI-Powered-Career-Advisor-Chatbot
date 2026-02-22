import streamlit as st
from backend.gemini_service import GeminiService
from backend.prompt_template import build_career_prompt
from backend.memory import update_chat_history

st.set_page_config(page_title = "AI Career Advisor", page_icon = "🎓")
st.title("🎓 AI Career Advisor")
st.write('Ask Guru about your Career Doubt')

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'message' not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_input = st.chat_input("Ask career doubt......")

if user_input:
    st.session_state.message.append({"role":"user","content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = build_career_prompt(
        user_input,
        st.session_state.chat_history
    )

    gemini_service = GeminiService()

    with st.chat_message('Guru'):
        with st.spinner('Thinking...'):
            response = gemini_service.generate_response(prompt)
            st.markdown(response)

    st.session_state.message.append(
        {"role":"assistant", "content": response}
    )

    st.session_state.chat_history = update_chat_history(
        st.session_state.chat_history,
        user_input,
        response
    )