from utils import extract_text_from_pdf, structured_ouput_extractor, json_output_extractor, print_dict
from prompts import system_prompt, user_prompt


pdf_path = "sample.pdf"
text = extract_text_from_pdf(pdf_path)
data = structured_ouput_extractor(text)

# Print customer details
print("Name:", data.customer_details.name)
print("Address:", data.customer_details.address)
print("Phone:", data.customer_details.contact.phone)
print("Email:", data.customer_details.contact.email)

# Print total amount details
print("Taxable Amount:", data.total_amount.taxable_amount)
print("IGST:", data.total_amount.IGST)
print("Round Off:", data.total_amount.round_off)
print("TCS:", data.total_amount.TCS)
print("Total:", data.total_amount.total)
print("Amount Payable:", data.total_amount.amount_payable)

# Print product details
for index, product in enumerate(data.products, start=1):
    print(f"Product {index} Name:", product.name)
    print(f"Product {index} Quantity:", product.quantity)
    print(f"Product {index} Price:", product.price)

data_2 = json_output_extractor(system_prompt, user_prompt, text)
print_dict(data_2)