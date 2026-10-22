from FormasGeometricas import Quadrado, Circulo

shapesList = {}    
            
def createShapes():
    
    shapeType = input('\n[1] QUADRADO\n[2] CIRCULO')

    match shapeType :

        case '1' :

            createSquare()

        case '2' : 

            createCircle()

def createSquare():

    numShapes = Quadrado.get_num_formas() + 1

    sideLength = float(input('Digite o comprimento do lado: '))

    shapeName = f'square{numShapes}'

    shapesList[shapeName] = Quadrado(f'Quadrado{numShapes}', sideLength)

    print(f'[{shapeName}] criado com sucesso!')

def createCircle():

    numShapes = Circulo.get_num_formas() + 1

    radius = float(input("Insira o raio do circulo: "))

    shapeName = f'circle{numShapes}'

    shapesList[shapeName] = Circulo(f'Circulo{numShapes}', radius)

    print(f'[{shapeName}] criado com sucesso!')

def serchShape(shapeName):

    for key in shapesList.keys() :

        if shapesList[key].get_name() == shapeName :

            return key



while True :

    print('\nFORMAS GEOMETRICAS')
    decision = input('\n[1] CRIAR\n[2] EXIBIR \n[3] MODIFICAR\n[4} EXCLUIR\n[5] SAIR\n')

    match decision :

        case '1' :

            createShapes()

        case '2' :
            
            for varName in shapesList.keys() :

                shape = shapesList[varName]

                print(shape.get_name(), end='')

                if isinstance(shape, Quadrado) :
                    
                    print(f' => lado: {shape.get_lado()}cm, area: {shape.area()}cm, {shape.perimetro()}cm')

                elif isinstance(shape, Circulo) :
                                    
                    print(f' => raio: {shape.get_raio()}cm, area: {shape.area()}cm, {shape.perimetro()}cm')

        case '3' :

            shapeWanted = input('Digite o nome da forma que deseja modificar: ')

            foundShape = shapesList[serchShape(shapeWanted)]

            if isinstance(foundShape, Circulo) :

                newRadius = float(input('Digite a nova medida do raio: '))

                foundShape.set_raio(newRadius)

            elif isinstance(foundShape, Quadrado) :

                newLength = float(input('Digite a nova medida do lado: '))

                foundShape.set_lado(newLength)

        case '4' :

            shapeWanted = input('Digite o nome da forma que deseja excluir: ')   

            keyOfShape = serchShape(shapeWanted)     

            del shapesList[keyOfShape]

        case '5' :

            break    
