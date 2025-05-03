# utils.py
from api_clients import openai_client, grok_client, groq_client

def get_response(prompt: str, model: str) -> str:
    if model == "OpenAI":
        if not openai_client:
            return "Greška: API ključ za OpenAI nije postavljen."
        try:
            resp = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specializing in creating resumes."},
                    {"role": "user",   "content": prompt},
                ],
            )
            return resp.choices[0].message.content
        except Exception as e:
            return f"Greška sa OpenAI API: {e}"

    elif model == "Grok":
        if not grok_client:
            return "Greška: API ključ za xAI (Grok) nije postavljen."
        try:
            resp = grok_client.chat.completions.create(
                model="grok-2-latest",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specializing in creating resumes."},
                    {"role": "user",   "content": prompt},
                ],
            )
            return resp.choices[0].message.content
        except Exception as e:
            return f"Greška sa xAI API: {e}"

    elif model == "Groq":
        if not groq_client:
            return "Greška: API ključ za Groq nije postavljen."
        try:
            resp = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Talk in Croatian. You are a helpful assistant specializing in creating resumes."},
                    {"role": "user",   "content": prompt},
                ],
            )
            return resp.choices[0].message.content
        except Exception as e:
            return f"Greška sa Groq API: {e}"

    else:
        return "Odaberi model."
