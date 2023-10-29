def elementos_repetidos(lista1, lista2):
    repetidos = False
    for elemento in lista1:
        if elemento in lista2:
            repetidos = True
            break
    if repetidos:
        print("Hay elementos repetidos de la lista 1 en la lista 2")
    else:
        print("No hay elementos repetidos de la lista 1 en la lista 2")
    repetidos = False
    for elemento in lista2:
        if elemento in lista1:
            repetidos = True
            break
    if repetidos:
        print("Hay elementos repetidos de la lista 2 en la lista 1")
    else:
        print("No hay elementos repetidos de la lista 2 en la lista 1")
# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
elementos_repetidos(lista1, lista2)