import random

def lanzar_varios_dados():
    
    # le pregunto al jugador cuantas veces quiere tirar
    veces = int(input("Cuantas veces quieres lanzar el dado? "))
    
    # aqui voy guardando la suma
    suma = 0
    
    # repito los lanzamientos
    for i in range(veces):
        numero = random.randint(1, 6)
        print("Lanzamiento", i+1, ":", numero)
        suma = suma + numero
    
    # al final muestro el total
    print("\nLa suma total es:", suma)

# ejecuto la funcion
lanzar_varios_dados()