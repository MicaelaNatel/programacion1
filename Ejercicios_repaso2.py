
#Ejercicio 1 
while True:
    word=input("Ingrese una palabra o frase: ")
    long=len(word)
    aux_word=word.replace(" ","")
    if not aux_word.isalpha():
        print("Ingrese solo letras, no numeros: ")
        continue
    else:
        if long == 4:
            print(f"{word}!")
        else:
            print(f"{word}?")  
        break 

#Ejercicio 2 Crea un juego donde el programa elija una word al azar de una lista y el usuario tenga que 
#adivinarla letra por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego.    
import random 
word=["programacion","laboratorio","matematica","sistema"]
random_palabra=random.randint(1,4)
attempts=6
while attempts<=6:
    letter=input("Ingrese la primer letra para adivinar la palabra: ")
    if letter == random_palabra[0]:
        print("letra correcta")
        continue
