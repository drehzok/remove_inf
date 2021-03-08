from pdf2image import convert_from_path

def convert_pdf_to_png(fname):
    pages = convert_from_path(fname, 500)
    for i, page in enumerate(pages):
        page.save(fname+str(i)+".png", "PNG")
