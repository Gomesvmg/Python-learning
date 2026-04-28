import random

PalavrasDoJogo = ['escola', 'lapis', 'borracha', 'caderno', 'cadeira']

aleNum = random.randint(0, len(PalavrasDoJogo)-1)

PalavraSelecionada = PalavrasDoJogo[aleNum]

print('Jogo da Forca')

numeroDeLetras = len(PalavraSelecionada)

LetrasDaPalavra = list(PalavraSelecionada)

display = ['_'] * numeroDeLetras #atencao


while True :

    for index in range(numeroDeLetras) :

        print(display[index].upper(), end='  ')

    if '_' not in display :

        print('\nVocê ganhou!')

        break

    Entrada = input('\n\nDigite uma letra: ')

    if  Entrada == '0' :

        break

    else : 

        cont = -1
        
        for cadaLetra in LetrasDaPalavra :

            cont += 1

            if Entrada == cadaLetra : 

                display[cont] = Entrada


