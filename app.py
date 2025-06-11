from flask import Flask, request, render_template
import fitz  # PyMuPDF
from transformers import pipeline

app = Flask(__name__)

# Extract text from uploaded PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Summarize using HuggingFace model
def summarize_text(text):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return summarizer(text[:1000], max_length=130, min_length=30, do_sample=False)[0]['summary_text']

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        file = request.files["pdf_file"]
        if file:
            file_path = "uploaded.pdf"
            file.save(file_path)
            extracted_text = extract_text_from_pdf(file_path)
            summary = summarize_text(extracted_text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
