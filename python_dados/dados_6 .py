import random

def lanzar_con_reporte():
    print("\n=== RETO 6: Lanzamientos con Reporte ===")
    
    total_tiros = 0
    suma_total = 0
    total_pares = 0
    total_impares = 0
    seguir = "si"
    
    while seguir == "si" or seguir == "s":
        numero = random.randint(1, 6)
        total_tiros = total_tiros + 1
        suma_total = suma_total + numero
        
        print(f"\nTiro #{total_tiros}: {numero}")
        
        if numero % 2 == 0:
            total_pares = total_pares + 1
        else:
            total_impares = total_impares + 1
        
        seguir = input("Deseas volver a lanzar? (si/no): ").lower()
    
    print("\n" + "="*40)
    print("REPORTE FINAL")
    print("="*40)
    print(f"Total de tiros efectuados: {total_tiros}")
    print(f"Suma total de los tiros: {suma_total}")
    print(f"Total de pares generados: {total_pares}")
    print(f"Total de impares generados: {total_impares}")
    print("="*40)
