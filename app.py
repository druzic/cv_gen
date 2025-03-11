import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from groq import Groq

# Učitavamo API ključ iz .env datoteke
load_dotenv()

# Vraćamo API ključ iz .env datoteke
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
XAI_API_KEY = os.getenv("XAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Provjeravamo da li je API ključ postavljen
if not OPENAI_API_KEY:
    st.error("Nema API ključa za OpenAI! Molimo postavite API ključ u .env datoteku.")
else:
    st.success("OpenAI API ključ je uspješno učitan!")

if not XAI_API_KEY:
    st.error("Nema API ključa za xAI! Molimo postavite API ključ u .env datoteku.")
else:
    st.success("xAI API ključ je uspješno učitan!")

if not GROQ_API_KEY:
    st.error("Nema API ključa za Groq! Molimo postavite API ključ u .env datoteku.")
else:
    st.success("Groq API ključ je uspješno učitan!")

# Inicializiramo OpenAI klijenta
if OPENAI_API_KEY:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)
clientGroq = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Implementacija konverzacijskog agenta za generiranje životopisa")
st.write("Streamlit je uspješno pokrenut!")

st.sidebar.title("Postavke")
models = st.sidebar.radio(
    "Koji model želite koristiti?",
    ["OpenAI", "Groq", "Grok", "Blenderbot"],
    index=None,
)


st.sidebar.write("Tvoj odabir:", models)


def get_response(prompt, model):
    if model == "OpenAI":
        if not OPENAI_API_KEY:
            return "Greška: API ključ nije postavljen"
        try:
            response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specializing in creating resumes."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Greška sa OpenAI API: {str(e)}"

    elif model == "Groq":
        if not GROQ_API_KEY:
            return "Greška: Groq API ključ nije postavljen."
        try:
            print(GROQ_API_KEY)
            chat_completion = clientGroq.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Talk on croatian language. You are a helpful assistant specializing in creating resumes."},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
                )
            print(chat_completion.choices[0].message.content)
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Greška sa Groq API: {str(e)}"

    elif model == "Grok":
        if not XAI_API_KEY:
            return "Greška: xAI API ključ nije postavljen"
        try:
            completion = client.chat.completions.create(
                model="grok-2-latest",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specializing in creating resumes."},
                    {"role": "user", "content": prompt},
                ],
            )
            print(completion.choices[0].message)
            return completion.choices[0].message.content
        except Exception as e:
            return f"Greška sa xAI API: {str(e)}"

    elif model == "Blenderbot":
        return "Blenderbot još nije implementiran."

    else:
        return "Odaberi model."


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    if models:
        agent_response = get_response(prompt, models)
        st.session_state.messages.append({"role": "assistant", "content": agent_response})

        # Display agent response in chat
        with st.chat_message("assistant"):
            st.markdown(agent_response)
    else:
        st.warning("Please select a model from the sidebar to proceed.")