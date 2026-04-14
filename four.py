from PyPDF2 import PdfReader, PdfWriter

# -----------------------------
# 1. Read PDF & Count Pages
# -----------------------------
def read_pdf(file_path):
    reader = PdfReader(file_path)
    print(f"Total Pages: {len(reader.pages)}")

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"\n--- Page {i+1} ---")
        print(text)


# -----------------------------
# 2. Merge PDFs
# -----------------------------
def merge_pdfs(pdf_list, output_file):
    writer = PdfWriter()

    for pdf in pdf_list:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_file, "wb") as f:
        writer.write(f)

    print("PDFs merged successfully!")


# -----------------------------
# 3. Split PDF
# -----------------------------
def split_pdf(input_pdf):
    reader = PdfReader(input_pdf)

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_file = f"page_{i+1}.pdf"
        with open(output_file, "wb") as f:
            writer.write(f)

    print("PDF split into individual pages!")


# -----------------------------
# 4. Search Keyword in PDF
# -----------------------------
def search_keyword(file_path, keyword):
    reader = PdfReader(file_path)
    found = False

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and keyword.lower() in text.lower():
            print(f"Keyword '{keyword}' found on page {i+1}")
            found = True

    if not found:
        print(f"Keyword '{keyword}' not found in PDF")


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    pdf1 = "file1.pdf"
    pdf2 = "file2.pdf"

    # Read and count pages
    read_pdf(pdf1)

    # Merge PDFs
    merge_pdfs([pdf1, pdf2], "merged.pdf")

    # Split PDF
    split_pdf(pdf1)

    # Search keyword
    search_keyword(pdf1, "Python")