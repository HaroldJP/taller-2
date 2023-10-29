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