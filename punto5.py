def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
print("El MCM de", x, "y", y, "es", lcm(x, y))