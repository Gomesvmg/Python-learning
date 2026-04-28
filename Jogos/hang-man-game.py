import random

PalavrasDoJogo = ['escola', 'lapis', 'borracha', 'caderno', 'cadeira']

aleNum = random.randint(0, len(PalavrasDoJogo)-1)

PalavraSelecionada = PalavrasDoJogo[aleNum]

print(PalavraSelecionada)

numeroDeLetras = len(PalavraSelecionada)

LetrasDaPalavra = list(PalavraSelecionada)

display = ['_'] * numeroDeLetras #atencao


while True :

    Entrada = input('Digite uma letra: ')

    if  Entrada == '0' :

        break

    else : 

        cont = -1
        
        for cadaLetra in LetrasDaPalavra :

            cont += 1

            if Entrada == cadaLetra : 

                display[cont] = Entrada

            print(display[cont].upper(), end=' ')
