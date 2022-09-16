# Initial commit 
# ps21-1727 Pamela Sanchez
# Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada 
# de la suma del cuadrado de ambos.

import math

# Se declara una variable y luego se intruce el digito que desea
numero1 = int(input("Introduzca un digito: "))
numero2 = int(input("Introduzca un digito: "))


# Se hacen las declaraciones de las operacion matematicas 
potencia1 = numero1**2
potencia2 = numero2**2
Suma_de_potencia = potencia1 + potencia2

# Ya aqui vemos el resultado de la operacion
print ("Numero 1 al cuadro es ", potencia1 )
print ("Numero 2 al cuadro es ", potencia2 )
print (" El resultado de la suma es ", Suma_de_potencia )
print ("Raiz cuadrada: ", math.sqrt(Suma_de_potencia))











 