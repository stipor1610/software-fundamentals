Funcion lanzar_dado
    Definir numero Como Entero
    
    numero <- Aleatorio(1, 6)
    
    Escribir ""
    Escribir "El dado cayo en: ", numero
    
    Si numero % 2 == 0 Entonces
        Escribir "El numero es PAR"
    SiNo
        Escribir "El numero es IMPAR"
    FinSi
FinFuncion

Algoritmo reto1
    lanzar_dado
FinAlgoritmo