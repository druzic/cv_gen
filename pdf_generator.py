# pdf_generator/generate_pdf.py

import pdfkit
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_pdf(data: dict) -> bytes:
    # 1. Postavi Jinja2 okruženje
    env = Environment(
        loader=FileSystemLoader(searchpath="templates"),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # 2. Učitaj HTML template
    template = env.get_template("cv.html")
    html_content = template.render(**data)

    # 3. Definiraj putanju do wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")  # <-- prilagodi ako ti je drugačije!

    # 4. Konvertiraj HTML u PDF i vrati bytes
    pdf_bytes = pdfkit.from_string(html_content, False, configuration=config)

    return pdf_bytes
