import pdfplumber


def extract_pdf_details(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Extract text from all pages
        all_text = ""
        for page in pdf.pages:
            #print(" text **" + page.extract_text())
            all_text += page.extract_text()

        # Extract other details as needed
        metadata = pdf.metadata
        num_pages = len(pdf.pages)

    return {
        "text": all_text,
        "metadata": metadata,
        "num_pages": num_pages
    }

# Example usage
#pdf_path = "C:/bills/Aug23/invoice 7.pdf"
#pdf_details = extract_pdf_details(pdf_path)

# Print extracted details
#print("Text:")
#print(pdf_details["text"])

#print("\nMetadata:")
#print(pdf_details["metadata"])

#print("\nNumber of Pages:")
#print(pdf_details["num_pages"])