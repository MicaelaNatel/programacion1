
name={}


players=int(input("Ingrese la cantidad de jugadores: "))
if  players<1 or players > 6:
     print("error")            
else:   
    for p in range(players):
        name[p+1] = input("Ingrese el nombre: ")
    print(name)
while True:
    number=int(input("Ingrese un numero del 1 al 6 o 0 para cerrar el programa: "))
    if  number >0 and number <7:
        print(number)
    elif number == 0:
        break
    else:
        print("El valor ingresado es incorrecto")
        continue
print("El juego ha finalizado")        

