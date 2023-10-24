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



```python
 import math

a = float(input("Ingrese un número real: "))
parte_entera, parte_decimal = math.modf(a)

digitos_enteros = []
digitos_decimales = []

while parte_entera > 0:
    digito = int(parte_entera % 10)
    digitos_enteros.append(digito)
    parte_entera //= 10

parte_decimal = abs(parte_decimal)
while parte_decimal > 0:
    digito = int(parte_decimal * 10)
    digitos_decimales.append(digito)
    parte_decimal = parte_decimal * 10 - digito

digitos_enteros.reverse()
print("Los digitos de la parte entera son:", digitos_enteros)
print("Los digitos de la parte decimal son:", digitos_decimales)
```
