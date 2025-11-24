def main():
    # Declarar variables
    num1 = 0.0
    num2 = 0.0
    
    # Solicitar entrada del primer número
    print("Enter the number 1")
    num1 = float(input())
    
    # Solicitar entrada del segundo número
    print("Enter the number 2")
    num2 = float(input())
    
    # Verificar si num1 > 0
    if num1 > 0:
        # Verificar si num1 es par o impar
        if num1 % 2 == 0:
            print(f"The first number {num1} & num1 & \"It's even\"")
        else:
            print(f"The first number {num1} & num1 & \"It's odd\"")
    else:
        # Verificar si num1 es par o impar (cuando num1 <= 0)
        if num1 % 2 == 0:
            print(f"The first number {num1} & num1 & \"It's even\"")
        else:
            print(f"The first number {num1} & num1 & \"It's odd\"")
    
    # Verificar si num2 > 0
    if num2 > 0:
        # Verificar si num2 es par o impar
        if num2 % 2 == 0:
            print(f"The second number {num2} & num2 & \"It's even\"")
        else:
            print(f"The second number {num2} & num2 & \"It's odd\"")
    else:
        # Verificar si num2 es par o impar (cuando num2 <= 0)
        if num2 % 2 == 0:
            print(f"The second number {num2} & num2 & \"It's odd\"")
        else:
            print(f"The second number {num2} & num2 & \"It's even\"")

if __name__ == "__main__":
    main()