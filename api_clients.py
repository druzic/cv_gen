from openai import OpenAI
from groq import Groq
from config import OPENAI_API_KEY, XAI_API_KEY, GROQ_API_KEY

# OpenAI client
openai_client = None
if OPENAI_API_KEY:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

# xAI (Grok) client
grok_client = None
if XAI_API_KEY:
    grok_client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )

# Groq client
groq_client = None
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)
