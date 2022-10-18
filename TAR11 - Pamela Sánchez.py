# Escriba una función que reciba 2 listas de productos (de forma dinámica), y retorne un conjunto
# (Set) de los productos comunes en las mismas. En caso de que no hayan productos comunes, retornar: 
# "No hay productos comunes en las listas".
# Pamela Sanchez 21-1727


print("====== Lista numero 01 ======")
# Creo una funcion, con una entrada por teclado y luego llamo la funcion para que funcione. 
def productos():
    cantidadD_Productos = int(input("Cuantos productos desea? "))
    return cantidadD_Productos


# Aqui creo dos lista para cuando el usuario ingrese los productos cada uno se guarde en la lista que va.
lista01 = []
lista02 = []


# Utilizo el bucle for y range para que itere las veces que el usuario desee.
for number in range(productos()):
    productos01 = (input("Producto: "))
    lista01.append(productos01.title())
print("Lista 01: ", lista01, "\n") 

# Aqui se repite lo mismo de arriba pero en una segunda lista.           
print("====== Lista numero 02 ======")
def productos02():
    cantidadD_Productos = int(input("Cuantos productos desea? "))
    return cantidadD_Productos

# Utilizo el bucle for y range para que itere las veces que el usuario desee.
for number in range(productos02()):
    productos02 = (input("Producto: "))
    lista02.append(productos02.title())
print("Lista 02: ", lista02)


# Convierto las listas en set para representar los conjuntos.
convertir01 = set(lista01)
convertir02 = set(lista02)

# Pongo una variable con el nombre cualquiera para poder hacer la interseccion con ambas listas
interseccion = convertir01.intersection(convertir02)

print ("\n" "*********************************************************************" "\n")

# aqui utilizo el if y el else para que me imprima cuando un producto se repite o cuando un producto no se repite en las listas.
if len(interseccion) == 0:
    print("No se repite ningun producto")
else:
    print("Los productos que se repiten son: " + str(interseccion))

print("\n""*********************************************************************""\n")
print("Hasta aqui llega mi programa, gracias por utilizarlo :)")

