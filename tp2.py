#TRABAJA MICA
#MICA GOD
#Ejercicio_1 verificar si el computador es nuevo o viejo
"""años_comp=int(input("Ingrese la cantidad de años de su computador: "))
if(años_comp>=0 and años_comp<=2):
   print("El computador es nuevo") 
elif(años_comp>2):
  print("El computador es viejo")
#Ejercicio_2-Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo. 
else:
  print("Ha ocurrido un error")"""
     

#Ejercicio_3-Solicitar al usuario dos nombre de dos personas, Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Sino imprimir ‘no hay coincidencia’.     
 
"""name_1=input("Ingrese el primer nombre: ")
name_2=input("Ingrese el segundo nombre: ")
name_1=name_1.lower()
name_2=name_2.lower()
if(name_1[0]==name_2[0]):
  print("Coincidencia")
else:
  print("No hay coincidencia") """ 
   
#Ejercico_4 Crear un programa que permita al usuario elegir un candidato por el cual votar. 
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, 
# candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: 
# ‘Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
# indicar ‘Opción errónea.’

print("Candidato A: Partido Rojo")
print("Candidato B: Partido Verde")
print("Candidato C: Partido Azul")
candidato=input("Ingrese (A,B,C) segun al candidato que desea votar: ")
candidato=candidato.lower()
if(candidato=="a"):
  print("Usted a votado por el Partido Rojo ")
elif(candidato=="b"):
  print("Usted a votado por el Partido Verde ")
elif(candidato=="c"):
  print("Usted a votado por el Partido Azul ")
else:
  print("Opcion erronea")  
