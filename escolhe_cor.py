
def define_cor(lista_012,palpite):
    i= 0
    caracteres_coloridos=[]
    while i<len(lista_012):
        letra=palpite[i]
        lis_numero=lista_012[i]
        if lis_numero==2:
            letra= f'\033[37m{letra}\033[m' 
            caracteres_coloridos.append(letra)

        if lis_numero==1:
            letra=f'\033[33m{letra}\033[m'
            caracteres_coloridos.append(letra)
        if lis_numero==0:
            letra=f'\033[34m{letra}\033[m'
            caracteres_coloridos.append(letra)
        i +=1
    return caracteres_coloridos
