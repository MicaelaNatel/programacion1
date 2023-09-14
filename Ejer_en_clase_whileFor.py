#Ejercicio 1
abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word=input("Escriba su palabra a encriptar: ")
word=word.lower()
long=int(input("Cuantos lugares quiere correr en su encriptado?: "))
longword=len(word)
for i in range(0,longword,1):
    if(word.isalpha()):
        position=abc.index(word[i])
        showedword=abc[(position+long)%27]
        print(f"{showedword}", end="")
    else:
        print(word[i])


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