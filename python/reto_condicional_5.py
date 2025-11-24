# Programa: Calculadora de incremento salarial
# Descripción: Calcula el nuevo salario según el género y salario actual

# Declaración de variables
tiDo = ""
nume = ""
noms = ""
apels = ""
gen = ""
aNa = 0
direc = ""
tel = ""
sala = 0.0
nueSala = 0.0
inc = 0.0

# Entrada de datos en las variables
print("Enter document type")
tiDo = input()

print("Enter ID number")
nume = input()

print("Enter names")
noms = input()

print("Enter last names")
apels = input()

print("Enter gender")
gen = input()

print("Year of birth")
aNa = int(input())

print("Address")
direc = input()

print("Phone")
tel = input()

print("Salary")
sala = float(input())

# Comparación de variable salario para realizar operaciones
if sala >= 2000000:
    # Salario mayor o igual a 2,000,000
    if gen == "female":
        # Mujer: incremento del 3%
        inc = (sala * 3) / 100
        nueSala = sala + inc
        print("The salary of ", noms, " ", apels, " is", nueSala)
    else:
        # Hombre: incremento del 2.5%
        inc = (sala * 2.5) / 100
        nueSala = sala + inc
        print("The salary of ", noms, " ", apels, " is", nueSala)
        
else:
    # Salario menor a 2,000,000
    if sala > 1200000 or sala > 2000000:
        # Salario entre 1,200,000 y 2,000,000: incremento del 5%
        inc = (sala * 5) / 100
        nueSala = sala + inc
        print("The salary of ", noms, " ", apels, " is", nueSala)
    else:
        # Salario menor o igual a 1,200,000
        if gen == "female":
            # Mujer: incremento del 10%
            inc = (sala * 10) / 100
            nueSala = sala + inc
            print("The salary of ", noms, " ", apels, " is", nueSala)
        else:
            # Hombre: incremento del 8%
            inc = (sala * 8) / 100
            nueSala = sala + inc
            print("The salary of ", noms, " ", apels, " is", nueSala)