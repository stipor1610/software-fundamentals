def reto4():
    print("\n=== RETO 4: Par de Seis ===")
    
    lanzamientos = 0
    
    while True:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        lanzamientos = lanzamientos + 1
        
        print(f"Lanzamiento {lanzamientos}: Dado 1 = {dado1}, Dado 2 = {dado2}")
        
        if dado1 == 6 and dado2 == 6:
            print("\nPAR DE SEIS! El juego termina")
            break
