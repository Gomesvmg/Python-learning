library = [
    ('Dom Casmurro', "Machado de Assis", 1899),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
    ("Vidas Secas", "Graciliano Ramos", 1938),
    ("Grande Sertão: Veredas", "Guimarães Rosa", 1956),
    ("Capitães da Areia", "Jorge Amado", 1937),
    ("A Hora da Estrela", "Clarice Lispector", 1977),
    ("Os Sertões", "Euclides da Cunha", 1902)
]

print('\nBIBLIOTECA DIGITAL\n')
#decision = str(input(''))


def visualizar(estante) :
    for titulo, autor, ano in estante:
        print(f"Obra: {titulo} | Escrito por: {autor} ({ano})")

visualizar(library)


