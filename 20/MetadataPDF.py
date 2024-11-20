#20. Lägg till metadata till en PDF-fil.

from PyPDF2 import PdfReader, PdfWriter

def add_metadata_to_pdf(input_pdf, output_pdf, metadata):
    try:
        # Läs in den befintliga PDF-filen
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
        
        # Kopiera alla sidor från original-PDF till den nya
        for page in reader.pages:
            writer.add_page(page)
        
        # Lägg till metadata
        writer.add_metadata(metadata)
        
        # Spara den nya PDF-filen med metadata
        with open(output_pdf, "wb") as file:
            writer.write(file)
        
        print(f"Metadata har lagts till i {output_pdf}")
    
    except Exception as e:
        print(f"Ett fel uppstod: {e}")

# Exempel på användning
if __name__ == "__main__":
    input_pdf_path = input("Ange sökväg till original-PDF: ")
    output_pdf_path = input("Ange sökväg för ny PDF med metadata: ")
    
    # Metadata att lägga till
    metadata = {
        "/Title": "Min titel",
        "/Author": "Mitt namn",
        "/Subject": "Ett exempel",
        "/Keywords": "Python, PDF, Metadata"
    }
    
    add_metadata_to_pdf(input_pdf_path, output_pdf_path, metadata)
