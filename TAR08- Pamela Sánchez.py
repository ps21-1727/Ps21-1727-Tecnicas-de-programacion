# Escriba un programa que, mediante una función, retorne las tablas de multiplicar del n al m.
# Ejemplo:
# Ingrese el número por el que comenzarán a mostrarse las tablas: 1
# Ingrese el número por el que terminarán a mostrarse las tablas: 3
# Pamela Sánchez 21-1727



# Declarar las variables y darle una entrada por teclado.
tablaInicio = int(input("Introduzca el numero por la tabla que quiere empezar: "))
print("\n")
tablaFinal = int(input("Introduzca por cuál numero quiere que termine su tabla: "))
print("\n")


def multiplicación (a, b):
    tablaMedio = 0
    # Se pone este while y su funcion es ejecutar hasta que sea verdadero, y en las demas lineas puse condiciones para que cumpla con cada funcion.
    while True:
        if tablaMedio == 0:
            print("\nTabla del: ", tablaInicio)
            for cifras in range(0,11):
                resultado = a*cifras
                print(a,"x", cifras, "=", resultado)
    
        if tablaMedio==tablaFinal-1:
            print("\nTabla del: ", tablaFinal)
            for cifras in range(0,11):
                    resultado = b*cifras
                    print(b,"x", cifras, "=", resultado)


        tablaMedio = tablaMedio+1



multiplicación(tablaInicio, tablaFinal)










    

 