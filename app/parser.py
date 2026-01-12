import re

PATTERN = re.compile(r'^(\d+(?:[.,]\d{1,2})?)\s+([a-zA-ZÀ-ÿ_]+)$')

def parse_message(text: str):
    if not text:
        return None
    match = PATTERN.match(text.strip())
    if not match:
        return None
    valor = match.group(1).replace(',', '.')
    categoria = match.group(2).lower()
    return valor, categoria
