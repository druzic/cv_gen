import streamlit as st
from config import check_keys
from utils import get_response
import json
from pdf_generator import generate_pdf
from test import test_cv_answers

if "show_expander" not in st.session_state:
    st.session_state["show_expander"] = True

st.set_page_config(page_title="Generator životopisa", page_icon="📝")

st.title("📝 Generator životopisa")
st.markdown(
    "### Brzo kreirajte profesionalni životopis\n"
    "Odgovorite na nekoliko pitanja uz pomoć konverzacijskog agenta i "
    "preuzmite gotov PDF dokument!"
)

with st.expander("ℹ️ Kako funkcionira?", expanded=st.session_state["show_expander"]):
    st.markdown(
        """
        1. **Odaberite** model u lijevom izborniku.
        2. **Vodite razgovor** s agentom – odgovorite na pitanja o iskustvu, obrazovanju i vještinama.
        3. Kada agent prikupi sve potrebne podatke, kliknite **Preuzmi životopis** i preuzmite PDF.
        """
    )

st.divider()



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
    index=1,
)
st.sidebar.write("Tvoj odabir:", model)

if st.sidebar.button("♻️ Nova sesija"):
    st.session_state.clear()
    st.rerun()

if st.sidebar.button("🧪 Testiraj moj životopis"):
    st.session_state.clear()
    st.session_state["messages"] = test_cv_answers.copy()
    st.session_state["test_mode"] = True
    st.rerun()


# session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# new user input
prompt = st.chat_input("Recite nešto…")
st.session_state["show_expander"] = False
if st.session_state.get("test_mode"):
    print("Testiranje")
    prompt = "  "  # dummy input da pokrene AI logiku
    st.session_state["test_mode"] = False

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response_stream = get_response(st.session_state.messages, model)
        #full_response = st.write_stream(response_stream)
        buffer= ""

        for chunk in response_stream:
            buffer += chunk


        try:

            cv_data = json.loads(buffer)
            st.session_state["cv_json"] = cv_data
            st.write("✅ Uspješno prikupljeni svi podaci! Generiram životopis...")
            st.session_state.messages.append({"role": "assistant", "content": "✅ Uspješno prikupljeni svi podaci! Generiram životopis..."})
            # session state prebaciti data
            #print(cv_data)
            progress = st.progress(0, text="Generiram PDF...")
            pdf_bytes = generate_pdf(cv_data)
            progress.progress(100, text="PDF generiran!")

            st.session_state["cv_pdf"] = pdf_bytes


            #funkcija za generiranje životopisa
        except json.JSONDecodeError:
            st.markdown(buffer)
            st.session_state.messages.append({"role": "assistant", "content": buffer})

    # JSON poruka
    # st.session_state.messages.append({"role": "assistant", "content": buffer})

if "cv_pdf" in st.session_state:
                st.download_button(
                label="📄 Preuzmi životopis",
                data=st.session_state["cv_pdf"],
                file_name="zivotopis.pdf",
                mime="application/pdf"
            )

