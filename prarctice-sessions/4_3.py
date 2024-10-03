from vertexai.generative_models import Part
from vertexai.generative_models import GenerativeModel

def process_pdf_number_of_tokens():
    #file_uri = "gs://bhagavan-bucket/genai-resources/beginners-must-do.pdf"
    file_uri = "gs://bhagavan-pub-bucket/project.pdf"
    
    pdf_file = Part.from_uri(file_uri, mime_type="application/pdf")
    
    prompt = "How many tokens can the model process?"
    
    model = "gemini-1.5-pro-001"
    contents = [pdf_file, prompt]
    
    multimodal_model = GenerativeModel(model)

    response = multimodal_model.generate_content(contents=contents)
    print(response.text)


process_pdf_number_of_tokens()