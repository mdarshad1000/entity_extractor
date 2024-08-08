from utils import extract_text_from_pdf, structured_ouput_extractor, json_output_extractor, print_structured_response, print_json_response
from prompts import system_prompt, user_prompt

# load the PDF file
pdf_path = "data/sample.pdf"
text = extract_text_from_pdf(pdf_path)

# Extract Key information using the latest Structured Output by OpenAI
data = structured_ouput_extractor(text)

# Extract Key information using the Json Output by OpenAI
data_2 = json_output_extractor(system_prompt, user_prompt, text)


# Print the extracted data by method 1
print_structured_response(data)

print()
print()
print()
# Print the extracted data by method 2
print_json_response(data_2)