# Realice un programa que replique la impresión de una factura, como la que se muestra a continuación:
# Indicaciones:
# Omitir las categorías de productos.
# Capturar nombre del cliente y mostrarlo al inicio de la factura.
# A diferencia de como se muestra en la imagen, INCLUIR una columna para la CANTIDAD del producto.
# Hay productos que no llevan ITBIS, por lo que el programa debe de controlar esto, de modo que en la columna de ITBIS se tenga 0.00 si el producto no lleva, o el valor correspondiente si lleva.
# Fórmula para el cálculo del ITBIS: (precio / 1.18) * 0.18.
# Los valores deben presentarse con 2 posiciones decimales (tal como en la imagen).
# Se debe evitar capturar data basura.
# Pamela Sanchez ps21-1727


# Se declara la variable para que el usuario digite su nombre
NombreCliente = (input("Escriba su nommbre: ")) 
# Espacio para que no se vea pegado
print(

)

# Declaro una lista para que los datos vayan almacenado en cada una que pertenece 
lista = []
cantidad = []

# Utilizo el bucle for con 5 iteracines
for p in range(5):

    # Declaro cada variable que necesito cada una con entrada por teclado, para que el usuario digite lo que desee
    productos = (input("Nombre del producto: "))
    precio = int(input("Digite el precio del producto: "))
    cantidad = int(input("Que cantidad de producto desea del elegido: "))

    # Aqui se calculara la cantidad del producto por el precio para poder saber cuanto hace cada cantidad con itbis y sin el 
    calculo = precio * cantidad
    Itbis = (precio / 1.18) * 0.18


    # Se iran impriendo los resultados de acuerdo vaya poniendo los productos 
    print("Precio sin ITBIS: RD$",calculo,"pesos dominicanos. " )
    print("Precio con ITBIS: RD$", Itbis,"pesos dominicanos. ")
    print(

    )
    lista.append(productos)
    lista.append(precio)
    lista.append(cantidad)

print(


)
# por ultimo imprime todo a pagar con itbis y sin el 

totalPagar = calculo + Itbis
totalPagarItbis = totalPagar / 1.18 * 0.18 
print("Su total a pagar es: RD$", totalPagar, "pesos dominicanos.")
print("Su total a pagar con ITBIS es: RD$", totalPagar, "pesos dominicanos.")
print("Gracias por su compra!! ")



   
    

