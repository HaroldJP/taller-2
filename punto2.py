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