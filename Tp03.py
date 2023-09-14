#ej 1
word=input("Ingrese una palabra: ")
for i in range(10):
    print(word) 
#ej 2

age=int(input("Digite su edad "))
for i in range(age):
    print(i+1) 

#ej 3

numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    impares = []

    for i in range(1, numero + 1):
        if i % 2 != 0:
            impares.append(str(i))
    
    resultado = ', '.join(impares)
    print(resultado)


#ej 4
numero=input("Ingrese un numero positivo: ")
long=len(numero)
numero=int(numero)
nums=[]
for a in range(long):
    for i in range(numero,0,-1):
         numero=str(numero)
         nums.append(numero)
         numero=int(numero)-1
    
    resultado = ', '.join(nums)
    print(resultado)


#ej 5

invest=int(input("Cuanto dinero desea invertir?: "))
anualinterest=int(input("De cuanto es su interes anual?: %"))
years=int(input("Por cuantos años durara su inversion?: "))
for i in range(0,years,1):
    invest=((invest*anualinterest)/100)+invest
    print(f"Usted genero en el año {i} {invest}")

#ej 6
nums=int(input("Ingrese la altura: "))
for i in range(0,nums+1):
    print("")
    for a in range(0,i):
        print("x",end="")
    
#ej 7

for i in range(1,11,1):
    print(i,"--------------")
    for a in range(1,11,1):
        print(i, " x ", a, " = ", i*a) 

#ej 8

num = int(input("Ingrese un numero entero: "))
val = 1


for i in range(1, num + 1, 2):
 
    for j in range(i, 0, -2):
        print(j, end=' ')
        val = j
  
    print()
    
#ej 9
contrasenia=input("Ingrese su contraseña: ")
contraseniaintento=[]
while(contrasenia!=contraseniaintento):
    contraseniaintento=input("Confirme su contraseña: ")

#ej 10
num=int(input("Ingrese un numero primo: "))
#Me vi un tutorial de como hacer esto profe no me rete porfa lo aprendi, es igual que pseint
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

if(is_prime(num)):
    print("Es primo")
else:
    print("No es primo")
   
#ej 11
word=input("Ingrese una palabra: ")
long=len(word)
for i in range(long,0,-1):
    print(word[i-1])

#ej 12
phrase=input("Escriba una frase: ")
letter=input("Escriba una letra a buscar: ")
long=len(phrase)
counter=0
for i in range(0,long,1):
    if(letter==phrase[i]):
        counter=counter+1
    
print(f"La letra {letter} aparece {counter} veces")

#ej 13
word=""
while(word!="salir"):
    print(word)
    word=input("")
    

#ej 14
number1=int(input("Ingrese el primer numero entero"))
number2=int(input("Ingrese el segundo numero entero"))

for i in range(0,number1+1,1):
    if(i%2==0 or i==0):
        print(i," par")
    else:
        print(i," impar")
        
for i in range(0,number2+1,1):
    if(i%2==0 or i==0):
        print(i," par")
    else:
        print(i," impar")
    

#ej 15

num = int(input("Por favor, introduce un número entero mayor que cero: "))


if num > 0:
    print(f"Los divisores de {num} son: ")
    
  
    for i in range(1, num + 1):
     
        if num % i == 0:
            print(i)


#ej 16
numbers=int(input("Cuantos numeros va a introducir?: "))
negativ=0
for i in range(0, numbers, 1):
    num=int(input("Digite su numero: "))
    if(num<0):
        negativ=negativ+1
print(f"Digito una cantidad de {negativ} numeros negativos  ")

#ej 17
#no vale este
"""phrase=input("Ingrese una frase: ")
long=len(phrase)
phrase=phrase.lower()
list=[]
for i in range(0,long,1):
    if(list!="a"):
        if (phrase[i]=="a"):
            list.append("a")
    if (list!="i"):
        if(phrase[i]=="i"):
            list.append("i")
    if (list!="e"):
        if(phrase[i]=="e"):
            list.append("e")
    if (list!="o"):
        if(phrase[i]=="o"):
            list.append("o")
    if (list!="u"):
        if(phrase[i]=="u"):
            list.append("u")
print(list)
"""
#Eso fue lo que intente hacer y no pude, si gusta me explicaria como hacerlo con el metodo de arriba, al final use el metodo de abajo pq lei en un foro la funcion not in
#ej 17 este si
phrase = input("Ingrese una frase: ")
phrase = phrase.lower()  
vocals   = []

for i in phrase:
    if i in "aeiou" and i not in vocals:
        vocals.append(i)

print(vocals)

#ej 18
fibonacci = [0, 1]
for i in range(2, 10):
    nextnum = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(nextnum)
print("Los primeros 10 números de la secuencia de Fibonacci son:")
for num in fibonacci:
    print(num)

#Ej 1

#Ej 19
tope = int(input("Ingrese la cantidad a la que quiere lograr ahorrar: "))
fondo = 0
while fondo<tope:
    deposito = int(input("Ingrese la cantidad que quiere depositar"))
    if deposito<0:
        print("El monto ingresado no puede ser menor que 0")
    else:
        fondo = fondo + deposito
print(f"Los fondos depositados fueron de: {fondo}")

#Ej 20
num = 1
acumulador = 0
while num!= 0:
    num = int(input("Ingrese un numero entero: "))
    acumulador =  num + acumulador
print(f"La sumatoria de los numeros es: {acumulador}")

#Ej 21
mayor = 0
num = 1
while num != 0:
    num = int(input("Ingrese un numero positivo: "))
    if num<0:
        print("El numero ingresado no es positivo")
    else:
        if num>mayor:
            mayor = num
print(f"El numero mayor ingresado es: {mayor}")

#Ej 22
numeros_pares = 0
while True:
    numero = int(input("Ingrese el numero entero positivo(-1 para finalizar el programa)"))
    if numero == -1:
        break
    if numero<=0:
        print("Por favor ingrese un numero positivo")
        continue
    suma = 0
    numtemp = numero
    while numtemp>0:
        suma += numtemp%10
        numtemp //= 10
    print(f"La sumatoria de los digitos del numero {numero} es: {suma}")
    if numero%2 == 0:
        numeros_pares += 1
print(f"La cantidad de numeros pares ingresados es de: {numeros_pares}")
#Ej 23 y 24
total = 0
while True:
    monto = float(input("Ingrese el monto de la compra(0 para salir)"))
    if monto == 0:
        break
    if monto<=0:
        print("Por favor ingrese un monto positivo")
        continue
    total = total + monto
if total > 1000:
    total = total - (total * 0.1)
print(f"El total del monto de las compras es de: {total}")

#Ej 25
facto = int(input("Ingrese el numero que quiere obtener su factorial: "))
factorial=0
if facto == 0:
    factorial = 1
elif facto< 0:
    print("Ingrese un numero positivo")
else:
    factorial = 1
    for i in range(1, facto+1):
        factorial *= i
print(f"El resultado es: {factorial}")