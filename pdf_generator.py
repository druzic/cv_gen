import pdfkit
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_pdf(data: dict, template_name: str = "cv.html") -> bytes:
    """Generate a PDF from structured data using a chosen HTML template."""
    env = Environment(
        loader=FileSystemLoader(searchpath="templates"),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template(template_name)
    html_content = template.render(**data)

    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")  # <-- prilagodi ako ti je drugačije!

    pdf_bytes = pdfkit.from_string(html_content, False, configuration=config)

    return pdf_bytes
