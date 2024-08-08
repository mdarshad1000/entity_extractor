from openai import OpenAI
import fitz
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
import json

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Pydantic models for the extracted data
class Contact(BaseModel):
    phone: str
    email: str

class CustomerDetails(BaseModel):
    name: str
    address: str
    contact: Contact

class Product(BaseModel):
    name: str
    quantity: str
    price: str

class TotalAmount(BaseModel):
    taxable_amount: str
    IGST: str
    round_off: str
    TCS: str
    total: str
    amount_payable: str

class Invoice(BaseModel):
    customer_details: CustomerDetails
    products: List[Product]
    total_amount: TotalAmount


# Function to extract text from PDF using fitz
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ''
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


# Structure Output Response Extractor using OpenAI and Pydantic 
def structured_ouput_extractor(data):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are an expert that extracts structured information from invoice texts, focusing on accuracy and relevance. Your task is to analyze the given text and extract specific details which are Customer Information, Products, and Total Amount"},
            {"role": "user", "content": data},
        ],
        response_format=Invoice,
    )
    response = completion.choices[0].message.parsed
    return response

# Helper function to print Pydantic Response in a pretty format
def print_structured_response(invoice, indent=0):
    def print_nested(data, indent):
        if isinstance(data, BaseModel):
            data = data.dict()
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, BaseModel)):
                    print(' ' * indent + str(key) + ":")
                    print_nested(value, indent + 4)
                elif isinstance(value, list):
                    print(' ' * indent + str(key) + ":")
                    for i, item in enumerate(value, start=1):
                        print(' ' * (indent + 4) + f"Item {i}:")
                        print_nested(item, indent + 8)
                else:
                    print(' ' * indent + str(key) + ":", str(value))
        else:
            print(' ' * indent + str(data))

    print_nested(invoice, indent)


def json_output_extractor(system_prompt, user_prompt, data):
    completion = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": data},
        ]
    )
    response = completion.choices[0].message.content
    res = json.loads(response)
    return res

# helper function to print the output in a pretty format
def print_json_response(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            print(' ' * indent + str(key) + ":")
            print_json_response(value, indent + 4)
        elif isinstance(value, list):
            print(' ' * indent + str(key) + ":")
            for i, item in enumerate(value, start=1):
                print(' ' * (indent + 4) + f"Item {i}:")
                if isinstance(item, dict):
                    print_json_response(item, indent + 8)
                else:
                    print(' ' * (indent + 8) + str(item))
        else:
            print(' ' * indent + str(key) + ":", str(value))

