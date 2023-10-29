import math
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    if len(numeros_ordenados) % 2 == 0:
        medio1 = numeros_ordenados[len(numeros_ordenados) // 2]
        medio2 = numeros_ordenados[len(numeros_ordenados) // 2 - 1]
        return (medio1 + medio2) / 2
    else:
        return numeros_ordenados[len(numeros_ordenados) // 2]
def calcular_promedio_multiplicativo(numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    return math.pow(producto, 1 / len(numeros))
def ordenar_ascendentemente(numeros):
    return sorted(numeros)
def ordenar_descendentemente(numeros):
    return sorted(numeros, reverse=True)
def calcular_potencia_mayor_menor(numeros):
    numeros_ordenados = sorted(numeros)
    mayor = numeros_ordenados[-1]
    menor = numeros_ordenados[0]
    return math.pow(mayor, menor)
def calcular_raiz_cubica_menor(numeros):
    numeros_ordenados = sorted(numeros)
    menor = numeros_ordenados[0]
    return math.pow(menor, 1 / 3)
def pedir_numeros():
    numeros = []
    for i in range(5):
        numero = float(input("Ingrese un número real: "))
        numeros.append(numero)
    return numeros
numeros = pedir_numeros()
promedio = calcular_promedio(numeros)
mediana = calcular_mediana(numeros)
promedio_multiplicativo = calcular_promedio_multiplicativo(numeros)
numeros_ascendentes = ordenar_ascendentemente(numeros)
numeros_descendentes = ordenar_descendentemente(numeros)
potencia_mayor_menor = calcular_potencia_mayor_menor(numeros)
raiz_cubica_menor = calcular_raiz_cubica_menor(numeros)
print("Promedio:", promedio)
print("Mediana:", mediana)
print("Promedio multiplicativo:", promedio_multiplicativo)
print("Números ordenados de forma ascendente:", numeros_ascendentes)
print("Números ordenados de forma descendente:", numeros_descendentes)
print("Potencia del mayor número elevado al menor número:", potencia_mayor_menor)
print("Raíz cúbica del menor número:", raiz_cubica_menor)