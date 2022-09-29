# Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.
# Indicaciones: 
# El monto del préstamo debe ser solicitado.
# Se debe solicitar la cantidad mensual que se desea pagar.
# Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.

from email import message

# Se declaran las variables pedidadas por el usuario y se le asigna entrada por teclado.
prestamoMonto = int(input("¿Qué cantidad desea solicitar? "))
mensualApagar = int(input("¿Cuánto pagara mensual? ")) 

# Se hace una operacion matematica para que determine en cuantos meses pagara su prestamo solicitado.
mesesPagar = prestamoMonto / mensualApagar


# Se utiliza un while true y mientras se cumpla la linea 14 pasara a la linea 20.
while True:

    print("Usted pagara en", mesesPagar, "meses")
    break