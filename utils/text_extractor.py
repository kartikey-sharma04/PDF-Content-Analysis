import fitz

def extract_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text_by_page = []

        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            text_by_page.append(text)
            print(f"[INFO] Text extracted from page {page_num}")

        doc.close()
        return text_by_page

    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")
        return []
