import Funciones
#Solicitar al usuario numeros hasta que ingrese cero
num=int(input("Numero a procesar: "))

while num!=0:
    print(f"Suma: {Funciones.add_digits(num)}")
    num= int(input("Numero a procesar: "))

#Mostrar la sumatoria de todos numeros y la suma de sus digitos


summation=0
num = int(input("Numero a procesar: "))

while num!=0:
    print(f"La suma de los numeros es: {Funciones.add_numbers(num)} ")
    

#El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5,y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?  
def most(a,b):
    if(a>b):
        return a
    else:
        return b

def least(a,b):
    if (a<b):
        return a
    else:
        return b   

x = int(input("Un numero: "))
y = int(input("Otro numero: "))

print(most(x-3, least(x+2, y-5)))