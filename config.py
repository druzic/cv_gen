# config.py
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
XAI_API_KEY    = os.getenv("XAI_API_KEY")
GROQ_API_KEY   = os.getenv("GROQ_API_KEY")

def check_keys():
    missing = []
    for name, key in [
        ("OpenAI", OPENAI_API_KEY),
        ("xAI",    XAI_API_KEY),
        ("Groq",   GROQ_API_KEY),
    ]:
        if not key:
            missing.append(name)
    return missing
