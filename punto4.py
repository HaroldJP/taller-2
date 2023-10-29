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