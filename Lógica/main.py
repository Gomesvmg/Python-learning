from formas import Quadrado, Circulo

# while True :
#     print('FORMAS GEOMETRICAS')
#     decision = input('\n[1] CRIAR\n[2] MODIFICAR \n[3] EXIBIR\n[4} EXCLUIR ')

#     match decision :

#         case 1 :
#             break
            
            
# def createShapes():
    
#     shapeType = input('\n[1] QUADRADO\n[2] CIRCULO')

#     match shapeType :

#         case 1 :

#             createSquare()

#         case 2 : 

#             createCircle()

# def createSquare():

#     sideLength = 

            



square1 = Quadrado('azul', 3)
square2 = Quadrado('Laranja')

# print(f'Quadrado 1 \nCor: {square1.get_cor()}')
# print('lado: ', square1.get_lado())
# print('Area: ', square1.area())
# print('Perimetro', square1.perimetro())

square1.set_lado(0)
print(square1.get_lado())


circle1 = Circulo('Amarelo', 4)
circle2 = Circulo('Verde')

print('Cor: ', circle1.get_cor())
print('Raio: ', circle1.get_raio())
print('Area: ', circle1.area())
print('Perimetro: ', circle1.perimetro())
