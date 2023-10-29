def elementos_faltantes(lista1, lista2):
    faltantes = []
    for elemento in lista1:
        if elemento not in lista2:
            faltantes.append(elemento)
    return faltantes
# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
faltantes = elementos_faltantes(lista1, lista2)
if faltantes:
    print("Los elementos faltantes en la lista 2 son:", faltantes)
else:
    print("No hay elementos faltantes en la lista 2")