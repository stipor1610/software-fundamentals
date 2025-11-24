# Programa: Calculadora con menú
# Descripción: Realiza operaciones matemáticas básicas entre dos números

# Declarar variables
num1 = 0.0
num2 = 0.0
res = 0.0
opt = 0

# Inicializar variables
num1 = 0
num2 = 0

# Obtener el primer número
print("Enter value to number 1:")
num1 = float(input())

# Obtener el segundo número
print("Enter value to number 2:")
num2 = float(input())

# Mostrar menú de operaciones matemáticas
print("Math menu: [1]. Add - [2]. Subs - [3]. Mult - [4]. Div - [5] All")
print("Press any option [1-5]")
opt = int(input())

# Evaluar la opción seleccionada
if opt == 1:
    # Suma
    res = num1 + num2
    print("Addition:", res)
    
elif opt == 2:
    # Resta
    res = num1 - num2
    print("Substraction:", res)
    
elif opt == 3:
    # Multiplicación
    res = num1 * num2
    print("Multiplication:", res)
    
elif opt == 4:
    # División
    if num2 == 0:
        print("It is not possible to divide by zero")
    else:
        res = num1 / num2
        print("Division:", res)
        
elif opt == 5:
    # Todas las operaciones
    if num2 == 0:
        print("Add:", num1 + num2)
        print("Subs:", num1 - num2)
        print("Mult:", num1 * num2)
        print("Div: El numero 2 no puede ser", num2)
    else:
        print("Add:", num1 + num2)
        print("Subs:", num1 - num2)
        print("Mult:", num1 * num2)
        print("Div:", num1 / num2)
        
else:
    # Opción inválida
    print("Option invalid")