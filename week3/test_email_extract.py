# Task 2: Extract Email Addresses
# a) Write regex to extract emails from text
# b) Implement:
# def extract_emails(text: str) -> list[str]
# c) Write test to remove duplicates using set
# d) Add test to ignore invalid emails:
# Example: abc@.com
# e) Explain:
# Simple vs strict email regex trade-offs


from email_extract import extract_emails
def test_extract_emails():
    text="contact here anil@gmail.com or info@yahoo.com"
    emails=extract_emails(text)
    assert "anil@gmail.com" in emails
    assert "info@yahoo.com" in emails
    assert len(emails)==2

def test_remove_duplicates():
    text="anil@gmail.com anil@gmail.com info@yahoo.com"
    emails=extract_emails(text)
    unique_emails=list(set(emails))
    assert len(unique_emails)==2
    assert "anil@gmail.com" in unique_emails
    assert "info@yahoo.com" in unique_emails

def test_ignore_invalid_emails():
    text="anil@gmail.com info@com abc@.com info@yahoo.com"
    emails=extract_emails(text)
    assert "anil@gmail.com" in emails
    assert "info@yahoo.com" in emails
    assert "info@com" not in emails
    assert "abc@.com" not in emails
