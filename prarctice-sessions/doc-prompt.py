import fitz  # PyMuPDF
from genai import GenAI

# Path to the PDF
pdf_path = '/home/saketh/generative-AI/prarctice-sessions/my-new-dog-pdf-version.pdf'

# 1. Open and Extract Text from the PDF
pdf_document = fitz.open(pdf_path)

# Extract text from all pages
pdf_text = ''
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    pdf_text += page.get_text("text") + "\n"

# Close the document after extraction
pdf_document.close()

print("Extracted Text from PDF:\n", pdf_text)

# 2. Initialize the GenAI model (using your API key)
model = GenAI(api_key="AIzaSyCuBQZP94FWv_Dpd4t4nse0n9XPxpxXf6I")

# 3. Use the extracted text as the prompt for the model
response = model.predict(prompt=pdf_text)

# Print the response from the model
print("Response from Model:\n", response)
