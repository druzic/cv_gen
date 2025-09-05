# IMPLEMENTACIJA KONVERZACIJSKOG AGENTA ZA GENERIRANJE ŽIVOTOPISA

Završni rad Autor: Dominik Ružić

Mentor: doc. dr. sc. Nikola Tanković

Sveučilište Jurja Dobrile u Puli, Fakultet informatike

## Installation

1. Create and activate a virtual environment (optional but recommended).
2. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root containing your API keys:

```bash
OPENAI_API_KEY=your-openai-key
XAI_API_KEY=your-xai-key
GROQ_API_KEY=your-groq-key
```

Setup wkhtmltopdf path in `pdf_generator`

The `WKHTMLTOPDF_PATH` value should point to the `wkhtmltopdf` executable. For example on Windows:
`C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe`.

## Running the app

Start the Streamlit application with:

```bash
streamlit run app.py
```

A browser window will open showing the chat interface. Select the desired model in the sidebar and start the conversation.

## Example usage

1. Run the command above to start the app.
2. Choose a model (OpenAI, Groq or Grok) in the sidebar.
3. Provide the requested information in the chat.
4. When the assistant finishes gathering data, click **"📄 Preuzmi životopis"** to download the generated PDF.
