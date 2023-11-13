from filtra_palavras import filtra
from inicializa_termo import inicializa
from indica_posicao_correta import indica_posicao
from palavras import PALAVRAS
from escolhe_cor import define_cor


def valida(tentativa_usuario):
    if tentativa_usuario=='desisto':
        return 'desistiu'
    
    elif len(tentativa_usuario)!=5:
        return 'Poxa, você digitou uma palavra com quantidade diferente da solicitada'

    elif tentativa_usuario not in lista_filtrada:
        return 'Poxa, essa palavra não existe'
    elif tentativa_usuario in dicionario_gerado['especuladas']:
        return 'Você já utilizou essa palavra' 
    else:
        return 'Vamos jogar!'
    
print(' =========================== ')
print('|','                         ','|') 
print('|','Bem-vindo ao Insper Termo','|')
print('|','                         ','|')
print(' ==== Design de Software === ')
print('                         ')
print('Comandos: desisto')
print('                         ')
print(' Regras:')
print('                         ')
print('- Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.')
print('- A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print(f'\033[34m. Azul\033[m',': a letra está na posição correta;')
print(f'\033[33m. Amarelo\033[m' ,':a letra, mas está na posição errada;')
print(f'\033[37m. Cinza\033[m',': a palavra não tem a letra.')
print('- Os acentos são ignorados;')
print('- As palavras podem possuir letras repetidas.')  
print('                         ')
print('Já tenho uma palavra! Tente advinhá-la!')
print('                         ')
print('Você tem 6 tentativa(s)')
   


inicia_jogo=True
status_jogo=True
while status_jogo:                 
    inicia_jogo=True
    mais_uma=input('Vamos jogar?[s/n] ')
    numero=5
    max_tentativas=6
    lista_filtrada=filtra(PALAVRAS,numero)
    dicionario_gerado=inicializa(lista_filtrada)
    
    if mais_uma=='s':
        print('Vou sortear uma palavra...')
        lista_colorida=['      ','      ','      ','      ','      ','      ']
        while inicia_jogo: 
            if max_tentativas>0:
                palavra_sorteada=dicionario_gerado['sorteada']
                print("    ")
                print("Você tem", max_tentativas, "tentativas")
                tentativa_usuario=input('Qual seu palpite? ').lower()
                valida_palpite=valida(tentativa_usuario)
                if valida_palpite=='desistiu':
                    tem_certeza=input('Você tem certeza?[s/n] ')
                    if tem_certeza=='s':
                        print('que pena...')
                        inicia_jogo=False

                if valida_palpite=='Poxa, você digitou uma palavra com quantidade diferente da solicitada':
                    print('Poxa, você digitou uma palavra com quantidade diferente da solicitada')
                
                if valida_palpite=='Poxa, essa palavra não existe':
                    print('Poxa, essa palavra não existe')
                    
                if valida_palpite=='Você já utilizou essa palavra':
                    print('Você já utilizou essa palavra')
                
                
                if valida_palpite=='Vamos jogar!':
                    dicionario_gerado['especuladas'].append(tentativa_usuario)
                    gera_lista012=indica_posicao(palavra_sorteada,tentativa_usuario)
                    letras_coloridas=define_cor(gera_lista012,tentativa_usuario)
                    lista_colorida[6-max_tentativas]=letras_coloridas
                    print(' --- --- --- --- ---')
                    print(f'| {lista_colorida[0][0]} | {lista_colorida[0][1]} | {lista_colorida[0][2]} | {lista_colorida[0][3]} | {lista_colorida[0][4]} |')
                    print(' --- --- --- --- ---')
                    print(f'| {lista_colorida[1][0]} | {lista_colorida[1][1]} | {lista_colorida[1][2]} | {lista_colorida[1][3]} | {lista_colorida[1][4]} |')
                    print(' --- --- --- --- ---')
                    print(f'| {lista_colorida[2][0]} | {lista_colorida[2][1]} | {lista_colorida[2][2]} | {lista_colorida[2][3]} | {lista_colorida[2][4]} |')
                    print(' --- --- --- --- ---')
                    print(f'| {lista_colorida[3][0]} | {lista_colorida[3][1]} | {lista_colorida[3][2]} | {lista_colorida[3][3]} | {lista_colorida[3][4]} |')
                    print(' --- --- --- --- ---')
                    print(f'| {lista_colorida[4][0]} | {lista_colorida[4][1]} | {lista_colorida[4][2]} | {lista_colorida[4][3]} | {lista_colorida[4][4]} |')
                    print(' --- --- --- --- ---')
                    print(f'| {lista_colorida[5][0]} | {lista_colorida[5][1]} | {lista_colorida[5][2]} | {lista_colorida[5][3]} | {lista_colorida[5][4]} |')
                    print(' --- --- --- --- ---')
                    if tentativa_usuario==palavra_sorteada:
                        print('Parabéns, você ganhou!!!')
                        dicionario_gerado['especuladas']=[]
                        lista_colorida=['      ','      ','      ','      ','      ','      ']
                        max_tentativas=6
                        break     
                    max_tentativas -=1

            else:
                print('Suas tentativas acabaram, tente novamente')
                break
    elif mais_uma=='n':
        print('Você vai desistir de primeira, calabreso?')
        print('Até a próxima')
        break
    else:
        print('Digite apenas o que foi solicitado, amigao')
    

