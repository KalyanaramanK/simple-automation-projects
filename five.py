import pytesseract
from PIL import Image
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import docx

# -----------------------------
# 1. OCR - Extract text from Image
# -----------------------------
def extract_text_from_image(image_path):
    try:
        # Set path if needed (Windows)
        # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"OCR Error: {e}"


# -----------------------------
# 2. Web Scraping
# -----------------------------
def extract_text_from_web(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all paragraph text
        paragraphs = soup.find_all('p')
        text = "\n".join([p.get_text() for p in paragraphs])

        return text.strip()
    except Exception as e:
        return f"Web Scraping Error: {e}"


# -----------------------------
# 3. PDF Extraction
# -----------------------------
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text.strip()
    except Exception as e:
        return f"PDF Error: {e}"


# -----------------------------
# 4. Word Document Extraction
# -----------------------------
def extract_text_from_word(docx_path):
    try:
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        return f"Word Error: {e}"


# -----------------------------
# 5. Consolidated Output
# -----------------------------
def main():
    image_path = "sample_image.png"
    url = "https://example.com"
    pdf_path = "sample.pdf"
    docx_path = "sample.docx"

    print("\n========== CONSOLIDATED TEXT OUTPUT ==========\n")

    image_text = extract_text_from_image(image_path)
    print("🖼 IMAGE TEXT:\n", image_text, "\n")

    web_text = extract_text_from_web(url)
    print("🌐 WEB TEXT:\n", web_text[:1000], "\n")  # limit long output

    pdf_text = extract_text_from_pdf(pdf_path)
    print("📄 PDF TEXT:\n", pdf_text[:1000], "\n")

    word_text = extract_text_from_word(docx_path)
    print("📝 WORD TEXT:\n", word_text[:1000], "\n")


if __name__ == "__main__":
    main()