# taller-2
### Punto 1
Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

```python
a = int(input("Ingrese un número entero: "))
digitos = []

while a > 0:
    digito = a % 10
    digitos.append(digito)
    a //= 10

digitos.reverse()
print(f"Los digitos del número son: {digitos}")
```
 ### Punto 2

Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.


```python
def reales():
    n = float(input("Ingrese un número real: "))
    a = int(n)
    b = n - a 
    lista1 = []
    while a > 0:
        digito = a % 10      
        a = a // 10      
        lista1.append(digito)     
    if len(lista1) == 0:           
        lista1 = [0]
    lista2 = []                    
    while b < 1:
        b *= 10              
    while b != int(b):
        lista2.append(int(b) % 10)  
        b *=  10            
    if not lista2:
        lista2 = [0]                      
    print("Los dígitos de la parte entera son:")
    print(lista1[::-1])
    print("Los dígitos de la parte decimal son:")
    print(lista2)
if __name__ == "__main__":
    reales()
```
### Punto 3

Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

```python
a = int(input("Escriba el primer número: "))
b = int(input("Escriba el segundo número: "))

def espejos(a, b):
    stra = str(a)
    strb = str(b)
    if stra == strb[::-1] and strb == stra[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    espejo = espejos(a, b)
    if espejo == True:
        print(f"Los números {a} y {b} son números espejos.")
    else:
        print(f"Los números {a} y {b} no son números espejos.")
```

### Punto 4

Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

```python
import math
def cos_aprox(x, n):
    aprox = 0
    for i in range(n):
        aprox += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return aprox
def main():
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese el número de términos de la serie: "))
    aprox = cos_aprox(x, n)
    real = math.cos(x)
    diferencia = abs(real - aprox)
    print("Aproximación:", aprox)
    print("Valor real:", real)
    print("Diferencia:", diferencia)
    umbral_10 = 0.1 * real
    umbral_1 = 0.01 * real
    umbral_01 = 0.001 * real
    umbral_001 = 0.00001 * real
    for i in range(n):
        aprox = cos_aprox(x, i)
        real = math.cos(x)
        diferencia = abs(real - aprox)
        if diferencia <= umbral_10:
            print("Error del 10% con", i, "términos")
        if diferencia <= umbral_1:
            print("Error del 1% con", i, "términos")
        if diferencia <= umbral_01:
            print("Error del 0.1% con", i, "términos")
        if diferencia <= umbral_001:
            print("Error del 0.001% con", i, "términos")
            break
if __name__ == "__main__":
    main()
```

### Punto 5

Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.


```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
print("El MCM de", x, "y", y, "es", lcm(x, y))
```

### Punto 6

Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.

```python
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
```

### Punto 7

Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

```python
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
lista = ["hola", "mundo", "Python", "XD"]
for cadena in lista:
    if tiene_vocales(cadena):
        print("La cadena", cadena, "tiene dos o más vocales")
    else:
        print("La cadena", cadena, "no tiene dos o más vocales")
```

### Punto 8

Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

```python
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
```

### Punto 9

Resolver el punto 7 del taller 1 usando operaciones con vectores.

```python
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
```

### Punto 10

Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?



```python
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
```
