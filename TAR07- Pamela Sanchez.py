#Escribir un programa que capture una lista de caracteres. 
#Indicaciones:
#La longitud de la lista debe ser dinámica (capturada).
#Si el usuario ingresa un dígito (cualquiera), se debe terminar la ejecución del programa con el mensaje: "Lo sentimos, no se permiten dígitos.", y mostrar la lista con los caracteres que se lograron capturar (en caso de que se hayan capturado).
#Si el usuario ingresa una palabra, se debe de omitir y continuar con el bucle.
#Mostra la lista con los caracteres capturados y el total.



# Se crea una lista, para cuando se haga la lista se almacene en esta variable. 
listaCapturada = []

# Se le da una entrada por teclado para que pueda introducir todos los caracteres que el usuario desee.
limiteCaracter = int (input("Introduzca la cantidad de caracteres que desee: "))


# Se usa el bucle while y hasta que no que cumpla con lo que se le pida el break lo estara devolviendo, hasta que si ponga lo que se le pide.
while len(listaCapturada) != limiteCaracter:
    letra = (input("Indroduzca el caracter: ")) # Se declara una variable letra, para que el usuario indrozca el caracter
    if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9":
        print("No se aceptan digitos")
        break
    elif len(letra) > 1:
        continue
    else:
        listaCapturada.append(letra)
print("La lista de palabra repetidas es: ",listaCapturada)
print(len("La cantidad de palabras repetidas es: ",listaCapturada))