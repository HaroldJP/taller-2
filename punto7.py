def tiene_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
            if contador >= 2:
                return True
        else:
            contador = 0
    return False

# Ejemplo de uso
lista = ["hola", "mundo", "Python", "programación"]
for cadena in lista:
    if tiene_vocales(cadena):
        print("La cadena", cadena, "tiene dos o más vocales")
    else:
        print("La cadena", cadena, "no tiene dos o más vocales")