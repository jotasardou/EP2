from random import choice
def inicializa(lista):
    out={}
    out['n']=len(lista[0])
    out['sorteada']=choice(lista)
    out['especuladas']=[]
    out['tentativas']=len(lista[0])+1
    return out

