import random

wordsOfGame = ['escola', 'lapis', 'borracha', 'caderno', 'cadeira']

index = random.randint(0, len(wordsOfGame)-1)

wordSelected = wordsOfGame[index]

print(wordSelected)

numberOfCharacters = len(wordSelected)

eachWord = list(wordSelected)

print('_ ' * numberOfCharacters)

while True :

    characterInput = input('Digite uma letra: ')

    if len(characterInput) > -1 :

        print(wordSelected.find(characterInput)) 

        for numLet, lett in enumerate(eachWord) :

            if characterInput == lett :

                print(characterInput, lett, 'pos: ', numLet)
