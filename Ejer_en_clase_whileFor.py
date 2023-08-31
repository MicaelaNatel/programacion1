#Ejercicio_1
cant_saltos=int(input("Ingrese la cantidad de saltos"))
for n in range(0,5,cant_saltos):


#Ejercicio_2
 total_imp=0 
 total_pares=0
while True:
    num=int(input("Ingrese un numero entero positivo,coloque 0 para finalizar: "))
    if num == 0:
        break
    pares=0
    imp=0
    digitos_pares=0
    digitos_imp=0

    n2=num 

    while n2 > 0:
        digito= n2 % 10
        if digito % 2 == 0:
            digitos_pares+=1
        else:
            digitos_imp+=1
        n2//=10
    pares+=digitos_pares
    imp+=digitos_imp
    print(f"digitos pares: {pares}")
    print(f"digitos impares: {imp}")
    total_pares+=digitos_pares
    total_imp+=digitos_imp


print(f"El total de digitos pares es: {total_pares}")          
print(f"El total de digitos impares es: {total_imp}")      