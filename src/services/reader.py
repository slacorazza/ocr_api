import fitz

def extract_text_fitz(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text("text", sort=True)
        print(f"\n--- Página {page_num} ---\n")
        print(page_text)
        text += page_text
    return text
