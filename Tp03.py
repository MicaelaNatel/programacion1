#Ejercicio 1
#Pedir una palabra al usuario
"""word=input("Ingrese una palabra: ")
#Mostrara 10 veces por pantalla
for w in range(10):
    print(word)

#Ejercicio 2
# Pedir edad al usuario   
age=int(input("Ingrese su edad: "))
#Ver cuantos anos han pasado
for (i) in range(age):
    print(i+1)

#Ejercicio 3 
#Pedir al usuario un numero
num=int(input("Ingrese un numero: "))
#Mostrar los impares 
for i in range(1,num+1,2):
   if i<num:  
     print(i,end=",")
   else:
     print(i)
     
#Ejercicio 4 
#Pedir al usuario un numero
num=int(input("Ingrese un numero: "))
#Mostrar el numero hasta el 0
for i in range(num,-1,-1):
   if i>0:  
     print(i,",",end="")
   else:
     print(i)
   
#Ejercicio 5 
amount=int(input("Ingrese la cantidad invertida: "))
interest=float(input("Ingrese el interes anual: "))
num_years=int(input("Ingrese el numero de años: "))
for i in range(num_years):
  amount=amount+(amount*(interest/100)) 
  print(f"En el ano {i} se gano {amount}")

#Ejercicio 6 
num=int(input("Ingrese una altura para el triangulo: "))
for i in range(1,num+1):
    print("*"*i)

#Ejercicio 7 Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10
num=10
for n in range(1,11):
    for i in range(1,11):
     board=(f"{n}x{i}={n*i}")
     print(board)

#Ejercicio 8 Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo."""



#Ejercicio 9 9-Escribir un programa que almacene la cadena de 
# caracteres contraseña en una variable, pregunte al usuario por 
# la contraseña hasta que introduzca la contraseña correcta.
