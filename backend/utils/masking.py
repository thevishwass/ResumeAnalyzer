# backend/utils/masking.py

import re
from email_validator import validate_email, EmailNotValidError

def mask_emails(text: str) -> str:
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    matches = re.findall(email_pattern, text)
    for email in matches:
        try:
            validate_email(email)
            text = text.replace(email, "[EMAIL REDACTED]")
        except EmailNotValidError:
            continue
    return text

def mask_phone_numbers(text: str) -> str:
    phone_pattern = r'\b(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b'
    return re.sub(phone_pattern, "[PHONE REDACTED]", text)
