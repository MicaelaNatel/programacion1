import math
#Ejercicio_1 verificar si el computador es nuevo o viejo
años_comp=int(input("Ingrese la cantidad de años de su computador: "))
if(años_comp>=0 and años_comp<=2):
   print("El computador es nuevo") 
elif(años_comp>2):
  print("El computador es viejo")
#Ejercicio_2-Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo. 
else:
  print("Ha ocurrido un error")
     

#Ejercicio_3
 
#Solicitar al usuario dos nombre de dos personas
name_1=input("Ingrese el primer nombre: ")
name_2=input("Ingrese el segundo nombre: ")
name_1=name_1.lower()
name_2=name_2.lower()
#Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra
if(name_1[0]==name_2[0]):
  print("Coincidencia")
else: #Sino imprimir ‘no hay coincidencia’
  print("No hay coincidencia") 
   
#Ejercico_4
print("Candidato A: Partido Rojo")
print("Candidato B: Partido Verde")
print("Candidato C: Partido Azul")
#SOlicitar al usuario que elija un partido
candidato=input("Ingrese (A,B,C) segun al candidato que desea votar: ")
candidato=candidato.lower()
#Verificar que partido eligio
if(candidato=="a"):
  print("Usted a votado por el Partido Rojo ")
elif(candidato=="b"):
  print("Usted a votado por el Partido Verde ")
elif(candidato=="c"):
  print("Usted a votado por el Partido Azul ")
else:
  print("Opcion erronea")


#Ejercicio 5

#Solicitar al usuario una letra
letra=input("Ingrese una letra: ")
letra=letra.lower()
cant=len(letra)
if(cant == 1):  
    #si es una vocal,mostrar el mensaje ‘Es vocal’.
    if (letra == "a" ):
      print("Es una vocal")   
    elif (letra == "e" ):
      print("Es una vocal")
    elif (letra == "i" ):
      print("Es una vocal")
    elif (letra == "o" ):
      print("Es una vocal")
    elif (letra == "u" ):
      print("Es una vocal")         
    else:
     print("No es una vocal")   
else: #Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
    print("No se puede procesar el dato ")
   
#Ejercicio 6

#Solicitar al usuario un año
año=int(input("Ingrese un año: "))
#Verificar si es bisiesto
if (año % 4 == 0 and  año % 100 != 0) or ( año % 400 == 0):
  print("Es un año bisiesto")
else: 
  print("No es un año bisiesto")

#Ejercicio 7  

#Solicitar tres numeros al usuario
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

#Verificar cual es el menor
if (n1<n2) and (n1<n3):
    print(f"El menor es: {n1}")
elif (n2<n1) and (n2<n3):  
    print(f"El menor es: {n2}")
elif (n3<n1) and (n3<n2):
    print(f"El menor es: {n3}")    

#Ejercicio 8

#Solicitar el usuario y la contrasena
usuario=input("Ingrese su usuario: ")
contras=input("Ingrese su contrasena: ")
usuario_correcto="Gwenevere"
contrs_correcta="excalibur"
#Verificar si el usuario y la contrasena son las correctas
if (usuario==usuario_correcto) and (contras==contrs_correcta):
    print("Usuario y contraseña correctos")
else:
    print("Acceso denegado")

#Ejercicio 9 

#Solicitar nombre y sexo al usuario
nombre=input("Ingrese su nombre: ")
sexo=input("Ingrese su sexo F/M: ")
#Verificar si pertenecen al grupo A o B
if(sexo == 'F' and nombre.lower() < 'm') or (sexo == 'M' and nombre.lower() > 'n'):
        grupo = "A"
        print("Usted pertenece al grupo A")
else:
        print("Usted pertenece al grupo B")

#Ejercicio 10 

#Solicitar edad al usuario
edad=int(input("Ingrese su edad: "))
#Verificar si paga o no
if edad < 4:
    print("Entra gratis")
elif edad > 4 and edad < 18:
    print("El costo de la entrada es $500")
else:
    print("El costo de la entrada es $1000") 

#Ejercicio 11       

print("Bienvenido a la pizzería Bella Napoli ")
print("OPCIONES: ")
print("1.Vegetariana")
print("1.No vegetariana")
#Preguntar al usuario que tipo de pizza quiere
opcion=int(input("Ingrese 1/2 segun la pizza que desea: "))
#Verificar si es vegetariana o no
if opcion == 1:
    #Mostrar ingredientes vegetarianos
    print("Usted a elegido una pizza vegetariana")
    print("Ingredientes vegetarianos: 1.Pimiento  2.tofu.")
    ingrediente=int(input("Ingrese 1/2 segun el ingrediente que desea agregar: "))
    if ingrediente == 1:
        print("Pizza Vegetariana: mozzarella, tomate y pimiento")
    else:
        print("Pizza Vegetariana: mozzarella, tomate y tofu")
elif opcion == 2: 
    #Mostrar ingredientes no vegetarianos
    print("Usted a elegido una Pizza No vegetariana")
    print("Ingredientes No vegetarianos: 1.Peperoni, 2.Jamón, 3.Salmón.")
    ingrediente=int(input("Ingrese 1/2/3 segun el ingrediente que desea agregar: "))
    if ingrediente == 1:
        print("Pizza No Vegetariana: mozzarella, tomate y peperoni")
    elif ingrediente == 2:
        print("Pizza No Vegetariana: mozzarella, tomate y jamon")
    else:
        print("Pizza No Vegetariana: mozzarella, tomate y salmon")          

#Ejercicio 12 

#Solicitar al usuario que ingrese el año
año_actual=int(input("Ingrese el año actual: "))
año_cual=int(input("Ingrese un año al azar: "))
#Verificar cuantos años han pasado 
if año_actual > año_cual:
    resultado=año_actual-año_cual
    print(f"Han pasado {resultado} años desde {año_cual} ")
else: #Verificar cuantos años faltan
    resultado=año_cual-año_actual
    print(f"Faltan {resultado} años para llegar a {año_cual} ")    

#Ejercicio 13 

#Solicitar dos numeros al usuario
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
#Verificar que no sea un numero negativo o nulo
if (n1<= 0) or (n2<=0):
    print(f"No debe ingresar un numero negativo o nulo")
else:
    #Verificar cual es el mayor y el menor
    if (n1 > n2):
       mayor=n1
       menor=n2
    else:
       mayor=n2
       menor=n1
#Verificar si es multiplo o no           
if mayor % menor == 0:
    print(f"El numero mayor: {mayor} es multiplo del numero menor: {menor}")
else:
     print(f"El numero mayor: {mayor} no es multiplo del numero menor: {menor}")    

#Ejercicio 14

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))
#Verificar si la ecuacion tiene o no solucion 
if (a == 0):
   if (b == 0):
      print("La ecuacion tiene infinitas soluciones")
   else:
      print("La ecuacion no tiene solucion")
#Verificar el resultado de la ecuacion       
else:
      resultado = ((-b)/a)
      if (resultado == -0.0):
           print("El resultado es: 0")
      else:
           print(f"El resultado es: {resultado}")   

#Ejercicio 15 

#Solicitar si quiere sacar el area de un triangulo o circulo
opcion=(int(input("Que area desea calcular, la de un triangulo o un circulo T/C: ")))
opcion=opcion.lower()
#Pedir los datos para el triangulo
if opcion == "t":
    base=float(input("Ingrese la base: "))
    altura=float(input("Ingrese la altura: "))
    area=(base*altura)/2
    print(f"El area del triangulo es: {area}")
#Pedir los datos para el circulo    
elif opcion == "c":
    radio=float(input("Ingrese el radio: ")) 
    area= math.pi * radio ** 2   
    print(f"El area del circulo es: {area}")

#Ejercicio 16 

#Pedir al usuario que ingrese dos numeros
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
#Solicitar al usuario que operacion desea realizar
print("Operacion 1:Suma")
print("Operacion 2:Multiplicacion")
print("Operacion 3:Resta")
print("Operacion 4:Division")
opcion=int(input("Ingrese el numero de operacion que desea realizar: "))
if opcion == 1:
    resultado= n1+n2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == 2:
    resultado= n1*n2
    print(f"El resultado de la multiplicacion es: {resultado}")
elif opcion == 3:
    resultado= n1-n2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == 4:
    resultado= n1/n2     
    print(f"El resultado de la division es: {resultado}")  

#Ejercicio 17    

#Pedir al usuario que ingrese un dia de la semana
dia=input("Ingrese un dia de la semana: ")
dia=dia.lower()
#Verificar que dia ingreso el usuario 
if dia == "lunes":
    print("Estamos en el dia lunes")
elif dia == "viernes":
    print("Estamos en el dia viernes") 
elif dia == "sabado" or dia == "domingo":
    print("Estamos en el dia sabado o domingo")    
else:
    print("Estamos en el dia martes, miercoles o jueves")     

#Ejercicio 18 

#Solicitar al usuario las horas trabajadas y salario x hora
horas = int(input("Ingrese la cantidad de horas trabajadas: "))
salario_hora = float(input("Ingrese su salario por hora: "))
#Verificar si ha hecho horas extras
if horas > 48:
      horas_extras = horas - 48
      horas = horas - horas_extras
      print(f"Usted trabajo un total de {horas_extras} hs extras")
      #Calcular salirio con las horas extras
      salario = horas * salario_hora + (((salario_hora*0.10)+salario_hora)*horas_extras)
      print(f"Su salario es de: {salario}")
else:#Calcular salario sin las horas extras
      salario = horas * salario_hora
      print(f"Su salario es de: {salario}")

#Ejercicio 19 

#Solicitar la cantidad de lapices comprados al usuario
cantidad=int(input("Ingrese la cantidad de lapices comprados: "))
#Calcular precio con descuento
if cantidad >= 1000:
      desc=60-(60*0.07)
      total=cantidad*desc
      print(f"El precio con descuento es: ${total}")
#Calcular precio sin descuento      
else:
      precio_final=cantidad*60
      print(f"El precio es: ${precio_final}")      

#Ejercicio 20 

nota = 0
cantidad = 0
for i in range(4):
        #Solicitar al usuario que ingrese sus notas
        nota_i = int(input("Ingrese la nota del alumno: "))
        nota = nota + nota_i
        cantidad = cantidad + 1
#Calcular el promedio        
promedio = nota / (cantidad)
print(f"El promedio de notas es de: {promedio}")
#Verificar si aprueba o desaprueba
if promedio<6:
        print("Desaprobado")
else:
        print("Aprobado")  