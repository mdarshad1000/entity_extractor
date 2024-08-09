# Entity Extractor
Entity Extractor is a python script designed to extract key information (Customer details, Products, Total Amount) from a PDF Invoice.

## Features

#### Structured Output Response
- Structured Outputs ensures the model will always generate responses that adhere to the supplied Pydantic Schema (which in this case has been prepared according to the Sample PDF provided), so you don't need to worry about the model omitting a required key, or hallucinating an invalid enum value.

#### JSON Output
- JSON Response also does the same job except that it's more flexible with the output provided.

### IMPORTANT POINT 
- Use `Structured Output Response` if all your PDF Invoices contain the same/similar fields to that of the provided sample PDF. Optionally, you can still change the Pydantic schema to suit your task.
- `JSON Output` is more flexible comparatively as it works for all type of PDF Invoices.

## SETUP
1. Create a `.env` and Set `OPENAI_API_KEY` as `OPENAI_API_KEY=sk-******************`
2. Install the requirements as:
```sh
pip install -r requirements.txt
```
3. Update the PDF path (optionally you can run it on the sample PDF) in `app.py`
```
pdf_path = "data/sample.pdf"
```
4. Run the script `app.py`
```sh
python3 app.py
```

#### EXAMPLE
1. STRUCTURED OUTPUT RESPONSE
```python
data = structured_ouput_extractor(text)
print_structured_response(data)
```

#### OUTPUT
```
customer_details:
    name: TEST
    address: Test, Hyderabad, TELANGANA, 500089
    contact:
        phone: 9108239284
        email: test@gmail.com
products:
    Item 1:
        name: WASTE AND SCRAP OF STAINLESS STEEL
        quantity: 6,790 KGS
        price: 6,45,050.00
total_amount:
    taxable_amount: ₹6,45,050.00
    IGST: ₹1,16,109.00
    round_off: 0.41
    TCS: ₹7611.59
    total: ₹7,68,771.00
    amount_payable: ₹7,68,771.00
```

2. JSON OUTPUT RESPONSE
```python
data = json_output_extractor(system_prompt, user_prompt, text)
print(data)
```

#### OUTPUT
```
{
  "CUSTOMER_DETAILS": {
    "name": "TEST",
    "billing_address": "Test, Hyderabad, TELANGANA, 500089",
    "contact_information": {
      "phone": "9108239284",
      "email": "test@gmail.com"
    }
  },
  "PRODUCTS": [
    {
      "name": "WASTE AND SCRAP OF STAINLESS STEEL",
      "quantity": "6,790 KGS",
      "price": "₹6,45,050.00"
    }
  ],
  "TOTAL_AMOUNT": {
    "taxable_amount": "₹6,45,050.00",
    "IGST": "₹1,16,109.00",
    "round_off": "0.41",
    "total": "₹7,68,771.00",
    "TCS": "₹7,611.59",
    "amount_payable": "₹7,68,771.00"
  }
}
```
  
3. JSON RESPONSE FOR IMAGE (Structured Output Response can also be used for images)
```python
data = json_output_extractor(system_prompt, user_prompt, image)
print(data)
```

#### OUTPUT
```
{
  "CUSTOMER_DETAILS": {
    "name": "TEST",
    "billing_address": "Hyderabad, TELANGANA, 500089",
    "contact_information": {
      "phone": "9108239284",
      "email": "test@gmail.com"
    }
  },
  "PRODUCTS": [
    {
      "name": "WASTE AND SCRAP OF STAINLESS STEEL",
      "quantity": "6,790 KGS",
      "price": "6,45,050.00"
    }
  ],
  "TOTAL_AMOUNT": {
    "taxable_amount": "6,45,050.00",
    "IGST": "1,16,109.00",
    "round_off": "0.41",
    "TCS": "27,611.50",
    "total": "7,68,771.00",
    "amount_in_words": "INR Seven Lakh, Sixty-Eight Thousand, Seven Hundred And Seventy-One Rupees Only"
  }
}
```
