from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(file_path, title, content):
    pdf_canvas = canvas.Canvas(file_path, pagesize=letter)
    pdf_canvas.setFont("Helvetica", 12)

    pdf_canvas.drawString(100, 800, title)

    y_position = 780
    for line in content:
        y_position -= 20
        pdf_canvas.drawString(100, y_position, line)

    pdf_canvas.save()

report_title = "My Report"
report_content = [
    "This is the first line of the report.",
    "This is the second line of the report.",
    "And so on..."
]

generate_report("my_report.pdf", report_title, report_content)
