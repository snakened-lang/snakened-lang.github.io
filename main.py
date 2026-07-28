import re

# 1. DEFINIÇÃO DOS TOKENS
TOKENS = [
    ('NUMBER',   r'\d+'),        
    ('PLUS',     r'\+'),         
    ('MINUS',    r'\-'),         
    ('MUL',      r'\*'),         
    ('DIV',      r'\/'),         
    ('SKIP',     r'[ \t]+'),     
    ('MISMATCH', r'.'),          
]

def lexer(codigo):
    tokens_encontrados = []
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKENS)
    for mo in re.finditer(token_regex, codigo):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            tokens_encontrados.append(('NUMBER', int(value)))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            print(f"❌ Erro na Snakened: Símbolo '{value}' não permitido!")
            return None
        else:
            tokens_encontrados.append((kind, value))
    return tokens_encontrados

def interpretador(tokens):
    if not tokens: return None
    resultado = tokens[0][1]
    i = 1
    while i < len(tokens):
        op = tokens[i][0]
        proximo_valor = tokens[i+1][1]
        if op == 'PLUS': resultado += proximo_valor
        elif op == 'MINUS': resultado -= proximo_valor
        elif op == 'MUL': resultado *= proximo_valor
        elif op == 'DIV':
            if proximo_valor == 0: return "Erro: Divisão por zero!"
            resultado /= proximo_valor
        i += 2
    return resultado

if __name__ == "__main__":
    print("🐍 SNAKENED v0.3 - Modo Interativo Ativo")
    while True:
        entrada = input(">> ")
        if entrada.lower() == 'sair': break
        tokens = lexer(entrada)
        if tokens:
            print(f"Resultado: {interpretador(tokens)}")
