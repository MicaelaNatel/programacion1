#Pedir dia,DD/MM al usuario 
fecha=(input("Ingrese el dia, DD/MM: ")) 
dia=(fecha[0:fecha.index(",")])
dd=int(fecha[fecha.index(" ")+1:fecha.index("/")])
mm=int(fecha[fecha.index("/")+1:])

 
#Convertir dia a minuscula
dia=dia.lower()
    
# Verifico que los dias ingresados sean los correctos 
if (dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="jueves" and dia!="viernes"):
   print("error")
   dia=input("Ingrese el dia de la semana nuevamente")

#Veo si las fechas numericas ingresadas son las correctas    
      
if(dd>31 or mm>12):
     print("Hubo un error en la fecha numerica")
     dd=input("Ingrese de nuevo el numero del dia en el que se encuentra: ")  
     mm=input("Ingrese el mes en el que se encuentra: ")

#Veo si pertenecen a nivel inicial,intermedio,avanzado
if((dia=="lunes")or(dia=="martes")or(dia=="miercoles")): 
      examenes=input("Se tomaron exames el dia de hoy? Y para si y N para no: ")
      examenes=examenes.lower()
      if(examenes=="y"):
         cant_aprob=int(input("Ingrese la cantidad de aprobados: "))
         cant_desap=int(input("Ingrese la cantidad de desaprobados: "))
         aprobados=(cant_aprob/(cant_aprob+cant_desap))*100
         print(f"La cantidad de aprobados es: {aprobados},%")       

#Veo si pertenecen a clases habladas
if(dia=="jueves"):
   asistencia=int(input("Ingrese el porcentaje de asistencia a clase: "))
   if(asistencia>=50):
      print("Asistio la mayoria")
   else:
      print("No asistio la mayoria")

#Veo si pertenecen a la clase de ingles para viajeros
if(dia=="viernes" and dd==1 and (mm==1 or mm==7)):
    print ("Comienzo de nuevo ciclo")
    alum_ingr=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
    arancel=int(input("Ingrese el arancel por cada alumno: "))
    ingr_total=(alum_ingr*arancel)
    print(f"El ingreso total es: ${ingr_total} ")

    