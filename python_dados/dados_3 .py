def reto3():
    print("\n=== RETO 3: Frecuencia de Numeros ===")
    
    veces = int(input("Cuantas veces quieres lanzar el dado? "))
    
    # contadores para cada numero
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    
    for i in range(veces):
        numero = random.randint(1, 6)
        print(f"Lanzamiento {i+1}: {numero}")
        
        if numero == 1:
            cont1 = cont1 + 1
        elif numero == 2:
            cont2 = cont2 + 1
        elif numero == 3:
            cont3 = cont3 + 1
        elif numero == 4:
            cont4 = cont4 + 1
        elif numero == 5:
            cont5 = cont5 + 1
        elif numero == 6:
            cont6 = cont6 + 1
    
    print("\n--- Resultados ---")
    print(f"El numero 1 salio {cont1} veces")
    print(f"El numero 2 salio {cont2} veces")
    print(f"El numero 3 salio {cont3} veces")
    print(f"El numero 4 salio {cont4} veces")
    print(f"El numero 5 salio {cont5} veces")
    print(f"El numero 6 salio {cont6} veces")
