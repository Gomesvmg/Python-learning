import math
pi = math.pi

def volumeDaEsfera(raio) :
    return pi *( (4/3) * (raio**3))

def qtdAgua(massa) :
    return massa * 0.03

def distPontos(x1, x2, y1, y2) :
    return math.sqrt((x1 - y1)**2 +(x2 - y2)**2)

def ordenar(n1, n2):
    if n1 > n2 :
        print(n2, n1)
    else :
        print(n1, n2)

def coleta(qtd) :
    nums = []
    for i in range(qtd) :
        n = int(input(f'n{i+1}: '))
        nums.append(n)
    return nums

def continuar():
    input('pressione para continuar')

while True:

    opcao = int(input('''PROVA PRÁTICA 1
        Escolha uma função:\n 
        [1]Volume da esfera
        [2]Quantidade de água diária
        [3]Distancia entre pontos
        [4]Ordenador de numeros
        [5]Sair
                    
    Opção: '''))

    match opcao:

        case 1:
            raio = float(input('Raio da esfera: '))
            print(f'Volume da esfera: {volumeDaEsfera(raio):.2f} cm³')
            continuar()

        case 2:
            massa = float(input('Digite a massa corporal (kg): '))
            print(f'Quantidade diária de água: {qtdAgua(massa)} L')
            continuar()

        case 3:
            coordenadas = coleta(4)
            print(f'Distância entre pontos: {distPontos(*coordenadas):.2f}')
            continuar()

        case 4:
            numeros = coleta(2)
            print(f'Números ordenados: {ordenar(*numeros)}')
            continuar()
        
        case 5:
            break
