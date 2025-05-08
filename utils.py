from api_clients import openai_client, grok_client, groq_client

def get_response(prompt: str, model: str):
    system_msg = {
        "role": "system",
        "content": "Talk in Croatian. You are a helpful assistant specializing in creating resumes."
    }
    user_msg = {"role": "user", "content": prompt}

    if model == "OpenAI":
        if not openai_client:
            yield "Greška: API ključ za OpenAI nije postavljen."
            return
        try:
            stream = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[system_msg, user_msg],
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Greška sa OpenAI API: {e}"
            return

    elif model == "Grok":
        if not grok_client:
            yield "Greška: API ključ za xAI (Grok) nije postavljen."
            return
        try:
            stream = grok_client.chat.completions.create(
                model="grok-2-latest",
                messages=[system_msg, user_msg],
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Greška sa xAI API: {e}"
            return

    elif model == "Groq":
        if not groq_client:
            yield "Greška: API ključ za Groq nije postavljen."
            return
        try:
            stream = groq_client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[system_msg, user_msg],
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Greška sa Groq API: {e}"
            return

    else:
        yield "Odaberi model."
        return
