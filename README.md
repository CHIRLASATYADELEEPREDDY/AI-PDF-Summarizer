#AI-PDF-SUMMARIZER

To run the AI PDF Summarizer, you need to install the following Python packages:

📦 Required Packages:
flask – for creating the web application
PyMuPDF – for reading and extracting text from PDF files (import fitz)
transformers – to access pre-trained AI models for summarization
torch – as the backend to run transformer models

Install them using:
pip install flask PyMuPDF transformers torch

🧠 About the Project
The AI PDF Summarizer is a web-based tool that allows users to upload PDF documents and receive a concise summary of their content using artificial intelligence. 
When a user uploads a PDF through the HTML form, the backend built with Flask handles the file and extracts its textual content using PyMuPDF. The extracted text 
is then passed to a transformer-based summarization model provided by the Hugging Face transformers library, which uses deep learning to understand and generate a 
human-like summary. The AI processing is supported by torch, which runs the language model efficiently in the background.

The summary is displayed instantly on the same page without refreshing or redirecting the user, providing a smooth and user-friendly experience. This tool is especially 
helpful for students, professionals, and researchers who need quick insights from lengthy documents. It is essential to have all the required packages installed, as the 
application will not work without them. Once everything is set up, you can start the Flask server, open the app in your browser, upload a PDF, and get an AI-generated 
summary in seconds.
