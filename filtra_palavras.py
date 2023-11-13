#aqui eu vou filtrar a lista gerada pelo professor como base de dados
#retornando apenas uma lista com caracteres minusculos, sem caractere especial e apenas com 5 letras
n=5
def filtra(PALAVRAS,numero):
    out=[]
    for palavra in PALAVRAS:
        palavra=palavra.lower()
        if len(palavra)==numero and palavra not in out:
            out.append(palavra)
    return out