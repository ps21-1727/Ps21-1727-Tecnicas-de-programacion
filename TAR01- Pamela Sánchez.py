#Primero se declaran las variables a utilizar
num1 = int(input(" Ingrese un digito: "))
num2 =  int(input("Ingrese otro digito: "))

#Segundo seleccionamos la operacion que queremos realizar
operacion = input("¿Que operacion desea relaizar suma, division, resta, multiplicacion? ")

#Por ultimo le pones la variable que operacion quiere al seleccionar
if operacion == "suma": 
    print("Resultado de la suma: ",num1+num2)


elif operacion == "division": 
    print("Resultado de la division: ",num1/num2)
    

elif operacion == "resta":
        print("Resultado de la resta: ",num1-num2)

elif operacion == "multiplicacion":
     print("Resultado de la multiplicacion: ",num1*num2)