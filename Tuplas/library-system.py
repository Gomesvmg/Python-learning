library = [
    ('Dom Casmurro', "Machado de Assis", 1899),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
    ("Vidas Secas", "Graciliano Ramos", 1938),
    ("Grande Sertão: Veredas", "Guimarães Rosa", 1956),
    ("Capitães da Areia", "Jorge Amado", 1937),
    ("A Hora da Estrela", "Clarice Lispector", 1977),
    ("Os Sertões", "Euclides da Cunha", 1902)
]

def view(estante) :

    for titulo, autor, ano in estante:

        print(f"Obra: {titulo} | Escrito por: {autor} ({ano})")

def search(method, info, storage):

    searchResult = []

    for book in storage:

        if book[method-1] == info:

            searchResult.append(book)

    return searchResult
            
print('\nBIBLIOTECA DIGITAL\n')

decision = int(input('Visualizar[1] Buscar[2] Adicionar[3]: '))

if decision == 1 : 

    view(library)

elif decision == 2 :

    type = int(input('Titulo[1] Autor[2] Ano[3]: '))
    searchInfo = str(input('Buscar por: '))
    
    print(f'Resultados encontrados: {search(type, searchInfo, library)}')
