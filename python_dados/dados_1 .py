import random

def lanzar_dado():
    
    numero = random.randint(1, 6)
    
    print(f"\n El dado cayó en: {numero}")
    
    if numero % 2 == 0:
        print(" El número es PAR")
    else:
        print(" El número es IMPAR")

lanzar_dado()
