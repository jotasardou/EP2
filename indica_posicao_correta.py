def indica_posicao(sorteada,palpite):
    lista=[]
    if len(sorteada)!=len(palpite):
        return []      
    i=0
    while i<len(palpite):
        letra=palpite[i]
        if letra in sorteada:
            caractere=sorteada[i]
            if letra==caractere:
                lista.append(0)
            else:
                lista.append(1)

        else:
            lista.append(2)
        i +=1
    return lista