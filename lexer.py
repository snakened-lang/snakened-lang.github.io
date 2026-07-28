import re

# O "Dicionário" da Snakened
TOKEN_TYPES = [
    ('KEYWORDS', r'\b(func|se|enquanto|escrever|retornar)\b'),
    ('TYPES',    r'\b(int|string|bool|float)\b'),
    ('ID',       r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER',   r'\d+'),
    ('STRING',   r'".*?"'),
    ('OP',       r'[+\-*/=<>!]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('SKIP',     r'[ \t\n]+'),
    ('MISMATCH', r'.'),
]

def lex(code):
    tokens = []
    regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_TYPES)
    for mo in re.finditer(regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'MISMATCH':
            continue
        tokens.append((kind, value))
    return tokens
