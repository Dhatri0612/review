# Task 2: Extract Email Addresses
# a) Write regex to extract emails from text
# b) Implement:
# def extract_emails(text: str) -> list[str]
# c) Write test to remove duplicates using set
# d) Add test to ignore invalid emails:
# Example: abc@.com
# e) Explain:
# Simple vs strict email regex trade-offs

import re
pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
def extract_emails(text: str)->list[str]:
    return re.findall(pattern,text)
