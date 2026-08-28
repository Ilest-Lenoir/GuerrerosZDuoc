import os
os.system("cls")


raza = {
    1: "SAYAYIN", 
    2: "NAMEKIANO", 
    3: "HUMANO", 
    4: "ANDROIDE"
                }



print(">> Sistema de Registro de Guerreros Z <<")
nombre=input("Ingrese nombre del guerrero: \n")
os.system("cls")

print(">> Sistema de Registro de Guerreros Z <<")
edad= int (input(f"Ingrese tu edad guerrero {nombre}: \n"))
os.system("cls")

print(">> Sistema de Registro de Guerreros Z <<")
opcion = int (input("""
Selecciona tu raza:
1) Sayayin <====
2) Namekiano <====
3) Humano <==== 
4) Androide <====
=======================\n"""))
os.system("cls")

raza_elegida = raza[opcion]

print(">> Sistema de Registro de Guerreros Z <<")
nivel_poder= int(input(f"Ingrese tu nivel de poder, {raza_elegida}!!:\n"))
os.system("cls")

if nivel_poder < 1000:
    SAYAYIN=print("No puede transformarse")
    os.system("cls")
    os.system("pause")
elif nivel_poder >= 1000 and nivel_poder <= 4999:
    SAYAYIN=print("Puede utilizar el Super Sayayin")
    duplicador= nivel_poder * 2
    SAYAYIN=print(f"Su nivel de poder ha incrementado a más de {duplicador}!! ")
    os.system("cls")
    os.system("pause")
elif nivel_poder >= 5000 and nivel_poder <= 9999:
    SAYAYIN=print("Puede utilizar el Super Sayayin 2!!")
    duplicador= nivel_poder * 3
    SAYAYIN=print(f"Su nivel de poder ha incrementado a más de {duplicador}!! ")
    os.system("cls")
    os.system("pause")
elif nivel_poder >= 10000:
    SAYAYIN=print("Puede utilizar el Super Sayayin 3!!!!")
    duplicador = nivel_poder * 4
    SAYAYIN=print(f"Su nivel de poder ha incrementado a más de {duplicador}!!!!!")
else: 
    nivel_poder >= 10000 and edad >= 18
    SAYAYIN=print(f"Das para combatir contra los dioses, guerrero {nombre} pero todavía no posees la madurez transformarte en uno de ellos..")
    SAYAYIN=print("Todavía no puedes utilizar el Super Sayayin 3...")
    