import re
import pandas as pd
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract

# Set Tesseract Path (IMPORTANT)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# -----------------------------
# Extract text from Image (OCR)
# -----------------------------
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# -----------------------------
# Extract Invoice Details using Regex
# -----------------------------
def extract_invoice_details(text):
    data = {}

    # Invoice Number
    invoice_no = re.search(r"(Invoice\s*No[:\s]*)(\w+)", text, re.IGNORECASE)
    data["Invoice Number"] = invoice_no.group(2) if invoice_no else "Not Found"

    # Date
    date = re.search(r"(\d{2}[-/]\d{2}[-/]\d{4})", text)
    data["Date"] = date.group(1) if date else "Not Found"

    # Billing Name (simple assumption)
    name = re.search(r"(Bill\s*To[:\s]*)([A-Za-z\s]+)", text, re.IGNORECASE)
    data["Billing Name"] = name.group(2).strip() if name else "Not Found"

    # Total Amount
    total = re.search(r"(Total\s*[:\s₹$]*)(\d+[\.,]?\d*)", text, re.IGNORECASE)
    data["Total Amount"] = total.group(2) if total else "Not Found"

    return data

# -----------------------------
# Process Invoice File
# -----------------------------
def process_invoice(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    return extract_invoice_details(text)

# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    files = [
        "invoice1.pdf",
        "invoice2.png"
    ]

    results = []

    for file in files:
        print(f"Processing: {file}")
        data = process_invoice(file)
        data["File Name"] = file
        results.append(data)

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Save to Excel
    df.to_excel("invoice_report.xlsx", index=False)

    # Save to CSV
    df.to_csv("invoice_report.csv", index=False)

    print("\n✅ Invoice data extracted and saved successfully!")