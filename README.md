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
