"""
Escriba un programa que, mediante el uso de funciones realice lo siguiente:

Dado un número entero, realice la suma de sus dígitos.
Con el resultado de la suma, realizar lo siguiente:
Generar los números del 1 al s (suma), y a su vez hacer las siguientes condiciones:
Si el número es divisor de 3, mostrar el número y la palabra "Fizz".
Si el número es divisor de 5, mostrar el número y la palabra "Buzz".
Si el número es divisor de 3 y 5 (ambos), mostrar el número y la palabra "FizzBuzz".
Si el número no es divisor de ninguno (3 y 5), únicamente mostrar el número.

Pamela Sánchez ps21-1727
"""
# Imprimo esto de primero para cuando el usuario ejecute el programa esto sea lo primero que vea.
print("==== FizzBuzz ====" "\n")


# Hago una entrada por teclado para que el usuario digite el número que desee hacer.
num = int(input("Introduzca un número: "))


# Aqui utilizo el bucle for para recorrer los elemntos de i y que sea iterrable.
for i in range (1,num):
    print(i)

    # Con la condicion if se ejecutara si es divisor de 3 y si no lo es tendra un elif para que sea el divisor de 5
    if i%3 == 0:
        print("Fizz" "\n")
    elif i%5 == 0:
        print("Buzz" "\n")
    # Aquí tengo un if que se cumple si el digito es divisor de ambas parte 
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz" "\n")

# Por último está condición se cumplirá si el número no es divisor de 3 o 5.        
if i%3 != 0 and i%5 != 0:
    print("Este número no es divisor ni de 3 ni de 5: ", num)
        
    

    
    