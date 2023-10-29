def multiplos_de_tres(lista):
    multiplos_acumulacion = []
    for num in lista:
        if num % 3 == 0:
            multiplos_acumulacion.append(num)
    multiplos_comprension = [num for num in lista if num % 3 == 0]

    return multiplos_acumulacion, multiplos_comprension
# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado_acumulacion, resultado_comprension = multiplos_de_tres(lista)
print("Enfoque de acumulación:", resultado_acumulacion)
print("Enfoque de comprensión de listas:", resultado_comprension)