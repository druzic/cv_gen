from api_clients import openai_client, grok_client, groq_client

def load_prompt(path="prompts/cv_agent.txt"):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def get_response(messages: list, model: str):
    system_msg = {
        "role": "system",
        "content": load_prompt(),
    }

    full_messages = [system_msg] + messages

    if model == "OpenAI":
        if not openai_client:
            yield "Greška: API ključ za OpenAI nije postavljen."
            return
        try:
            stream = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=full_messages,
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
                messages=full_messages,
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
                messages=full_messages,
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
