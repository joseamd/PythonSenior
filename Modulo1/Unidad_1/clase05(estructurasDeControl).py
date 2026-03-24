## ESTRUCTURAS DE CONTROL Y FLUJO
"""

#---
print("punto 1: \n")

a = 1

#operador de comparacion que de como resultado un true o false

print(a<5)

#---
print("punto subsisdio salario: \n")

sueldo=int(input("ingrese el sueldo del empleado: "))
if sueldo < 2000000:
    print("se cumplio el requisito para aplicar al subsidio")
    sueldo += 200000
else:
    print("no cumple el requisito para aplicar al subsidio.")
print ("ahora su sueldo es de " + str(sueldo) + "$ pesos")
"""
#---

"""
print("punto mayor de edad: \n")

nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad: "))

if edad >= 18:
    print(f"{nombre} es mayor de edad, ya que tiene {edad} años")
else:
    print(f"{nombre} no es mayor de edad ya que tiene {edad} años")
    
#---
print("punto etapas edad: \n")    

edad = int(input("ingrese la edad: "))

if edad < 0:
    print("edad no valida.")
elif edad < 5:
    print("esta en la etapa de primera infancia")
elif edad < 12:
    print("esta en la etapa de infancia")
elif edad < 17:
    print("esta en la etapa de adolensecia")
else:
    print("es mayor de edad")
"""

#---

"""
print("punto dia de la semana \n")

diaSemana=int(input("ingrese un numero del 1 al 7: "))

if diaSemana < 1:
    print("INGRESE UN NUMERO MAYOR ENTRE EL 1 Y EL 7 \n")


if diaSemana == 1:
    print("el dia de la semana es lunes \n")
if diaSemana == 2:
    print("el dia de la semana es martes \n")
if diaSemana == 3:
    print("el dia de la semana es miercoles \n")
if diaSemana == 4:
    print("el dia de la semana es jueves \n")
if diaSemana == 5:
    print("el dia de la semana es viernes \n")
if diaSemana == 6:
    print("el dia de la semana es sabado \n")
if diaSemana == 7:
    print("el dia de la semana es domingo \n")


if diaSemana >7:
    print("INGRESE UN NUMERO MAYOR ENTRE EL 1 Y EL 7 \n")
"""

#---
## otro condicional con match, que empareja la entrada con el caso, asi:

"""
print("punto condicional CASE: \n")

day = int(input("ingrese el numero del 1 al 7: "))

match  day:
    case 1:
        print("el dia de la semana es lunes \n")
    case 2:
        print("el dia de la semana es martes \n")
    case 3:
        print("el dia de la semana es miercoles \n")
    case 4:
        print("el dia de la semana es jueves \n")
    case 5:
        print("el dia de la semana es viernes \n")
    case 6:
        print("el dia de la semana es sabado \n")
    case 7:
        print("el dia de la semana es domingo \n")
    case _:
        print("INGRESE UN NUMERO EN EL RANGO SOLICITADO \n")
"""

#---

"""
print("punto CASE animal")

animal = input("seleccione entre terian, perro, gato o pez: ")

match  animal:
    case "gato":
        print("el gato hace miau \n")
    case "pez":
        print("el pez hace blub \n")
    case "perro":
        print("el perro hace gwau\n")
    case "terian":
        print("el terian es raro\n")
    case _:
        print("ingrese una opcion valida\n")

"""


#----


#CICLO WHILE

"""
i = 1

while i <= 5:
    print(i)
    i += 1

print("el ciclo finalizo en ", i)

"""

#---
"""
numeroTabla = int(input("ingrese un numero: "))
i=1
while i<=10:
    print(i*numeroTabla)
    i+=1
"""
#---

print("punto while, tabla de multiplicar \n")

numero = int(input("ingrese el numero del que quiere ver la tabla de multiplicar: "))
i = 1
while i <= 10:
    tabla = i*numero
    print (f"{numero} x {i} = {tabla}")
    i+=1
print("esa es la tabla de multiplicar del ", numero)
