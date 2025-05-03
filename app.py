# app.py
import streamlit as st
from config import check_keys
from utils import get_response

st.set_page_config(page_title="Generator životopisa", page_icon="📝")
st.title("Implementacija konverzacijskog agenta za generiranje životopisa")

# check for missing keys
missing = check_keys()
if missing:
    for svc in missing:
        st.error(f"Nema API ključa za {svc}! Molimo postavite API ključ u .env datoteku.")
else:
    st.success("Svi API ključevi su uspješno učitani!")

st.sidebar.title("Postavke")
model = st.sidebar.radio(
    "Koji model želite koristiti?",
    ["OpenAI", "Groq", "Grok"],
    index=0,
)
st.sidebar.write("Tvoj odabir:", model)

# session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# new user input
prompt = st.chat_input("Recite nešto…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = get_response(prompt, model)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
