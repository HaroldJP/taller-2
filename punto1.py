a = int(input("Ingrese un número entero: "))
digitos = []

while a > 0:
    digito = a % 10
    digitos.append(digito)
    a //= 10

digitos.reverse()
print(f"Los digitos del número son: {digitos}")
