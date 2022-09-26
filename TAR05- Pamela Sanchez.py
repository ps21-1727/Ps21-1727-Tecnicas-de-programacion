#Escriba un programa que pregunte al usuario los números de su ticket de lotería,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
#ps21-1727 Pamela Sanchez 


#Se pone un nombre para la lista
ticket_loteria = []

#se pone el bucle for con seis vueltas, se introducen los numeros en la variable numero
for n in range(6):
    numero =int(input("Introduzca los numeros: "))

#aqui se almacenan todos los numeros
    ticket_loteria.append(numero)

#se pone la lista organizada
ticket_loteria.sort()  

#se imprimen los numeros en orden ascendente
print("Su ticket de loteria ordenado es ", ticket_loteria)  
   
    
  