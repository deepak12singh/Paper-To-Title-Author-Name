#pip install PyPDF2 PyMuPDF pdfplumber slate3k camelot-py[cv] tika pdfquery pdfminer.six
  # PyMuPDF


def read_first_page_pypdf2(pdf_path):
    import PyPDF2
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            first_page = reader.pages[0]
            content = first_page.extract_text()
            return content if content else "No text found."
    except Exception as e:
        return f"PyPDF2 failed: {e}"


def read_first_page_pymupdf(pdf_path):
    import fitz
    try:
        with fitz.open(pdf_path) as pdf:
            first_page = pdf.load_page(0)
            content = first_page.get_text()
            return content if content else "No text found."
    except Exception as e:
        return f"PyMuPDF (fitz) failed: {e}"



def read_first_page_slate(pdf_path):
    import slate3k as slate
    try:
        with open(pdf_path, "rb") as file:
            document = slate.PDF(file)
            return document[0] if document else "No text found."
    except Exception as e:
        return f"Slate failed: {e}"


def read_first_page_camelot(pdf_path):
    import camelot
    try:
        tables = camelot.read_pdf(pdf_path, pages='1')
        if tables:
            return tables[0].df.to_string()  # Return the first table as a string
        else:
            return "No tables found."
    except Exception as e:
        return f"Camelot failed: {e}"


def read_first_page_tika(pdf_path):
    from tika import parser
    try:
        parsed = parser.from_file(pdf_path, xmlContent=True)
        content = parsed['content'].split("\n")[0]  # Get the first line of content
        return content if content else "No text found."
    except Exception as e:
        return f"Tika failed: {e}"


def read_first_page_pdfquery(pdf_path):
    import pdfquery
    try:
        pdf = pdfquery.PDFQuery(pdf_path)
        pdf.load()
        content = pdf.tree.xpath('//LTTextLineHorizontal/text()')[0]  # Get the first text line
        return content if content else "No text found."
    except Exception as e:
        return f"PDFQuery failed: {e}"


def read_first_page_pdfminer(pdf_path):
    from pdfminer.high_level import extract_text
    try:
        content = extract_text(pdf_path, page_numbers=[0])
        return content if content else "No text found."
    except Exception as e:
        return f"pdfminer failed: {e}"



def read_first_page_pdfplumber(pdf_path):
    import pdfplumber
    try:
        with pdfplumber.open(pdf_path) as pdf:
            first_page = pdf.pages[0]
            content = first_page.extract_text()
            return content if content else "No text found."
    except Exception as e:
        return f"pdfplumber failed: {e}"


"""
this is the call able function pdfminer
"""
def read_first_page(pdf_path):
    content = read_first_page_pdfplumber(pdf_path)
    if content == 'No text found.':
        content = ''
    return content

def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    # Example usage
    pdf_path = "file.pdf"  # Make sure 'file' is defined in your config or replace it with your PDF path

    # Call each function separately and save output
    results = {
        "PyPDF2": read_first_page_pypdf2(pdf_path),# not use this 3\10
        "PyMuPDF": read_first_page_pymupdf(pdf_path),# 5\10
        "pdfplumber": read_first_page_pdfplumber(pdf_path),# 9\10
        "Slate": read_first_page_slate(pdf_path),# 0\10
        "Camelot": read_first_page_camelot(pdf_path),#0\10
        "Tika": read_first_page_tika(pdf_path),#0\10
        "PDFQuery": read_first_page_pdfquery(pdf_path),#0\10
        "pdfminer": read_first_page_pdfminer(pdf_path) #5\10
    }

    # Save each result to a separate file
    for library_name, content in results.items():
        filename = f"{library_name}.txt"
        save_to_file(filename, content)
        print(f"Saved {library_name} output to {filename}")