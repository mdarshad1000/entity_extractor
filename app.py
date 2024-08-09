from utils import extract_text_from_pdf, structured_ouput_extractor, json_output_extractor, print_structured_response, extract_text_from_images
from prompts import system_prompt, user_prompt

# load the PDF file
pdf_path = "data/sample.pdf"
pdf_text = extract_text_from_pdf(pdf_path)


# Extract Key information using the latest Structured Output by OpenAI
data = structured_ouput_extractor(pdf_text)
print_structured_response(data)

# Extract Key information using the Json Output by OpenAI
data_2 = json_output_extractor(system_prompt, user_prompt, pdf_text)
print(data_2)

# For IMAGE
image_text = extract_text_from_images("data/Image.png")

data_3 = json_output_extractor(system_prompt, user_prompt, image_text)
print(data_3)