#Escriba un programa con funciones definidas por usted, que realice lo siguiente:
#Almacene una lista de 10 tuplas que correspondan a los siguientes viajeros de un aeropuerto. Nota: La estructura 
# de los datos de cada viajero es Nombre, Edad, Destino:
#Juan, 30, Madrid.
#Fernanda, 42, Portugal.
#Raúl, 28, Brazil.
#Julio, 32, Venezuela.
#Mateo, 26, Argentina.
#María, 32, Portugal.
#José, 29, Madrid.
#Marcos, 29, Venezuela.
#Juana, 41, Venezuela.
#Paulina, 35, Madrid.
#Muestre los destinos almacenados (sin repetir).
#Devuelva una lista de diccionarios de los pasajeros cuyo destino sea el solicitado por teclado.
#Si se coloca un destino que no se encuentra en los almacenados, el programa debe mostrar un mensaje diciendo:
#"No hay pasajeros para este destino".

# Pamela Sánchez 21-1727 

print("========================= Viajeros con Destinos Diferentes =========================""\n")
TuplasLista = [
    ('Juan', 30, 'Madrid'),
    ('Fernanda', 42, 'Portugal'),
    ('Raúl', 28, 'Brazil'),
    ('Julio', 32, 'Venezuela'),
    ('Mateo', 26, 'Argentina'),
    ('María', 32, 'Portugal'),
    ('José', 29, 'Madrid'),
    ('Marcos', 29, 'Venezuela'),
    ('Juana', 41, 'Venezuela'),
    ('Paulina', 35, 'Madrid')
]


# Creo las listas para que cada informacion vaya a donde tiene que ir y se guarde en forma de lista

Diccionario_01 = []
Destinatarios = []


# Hago el uso de un for para que imprima cada datos de los que estan en las tuplas salga identificado con nombre, edad y destino
# Hago una funcion y luego mas abajo la llamo para que se imprima
def CrearDiccionario(TuplasLista):
    for passw in TuplasLista:
        Diccionario = {}
        Diccionario ["Nombre"] = passw [0]
        Diccionario ["Edad"] = passw [1]
        Diccionario ["Destino"] = passw [2]
        Diccionario_01.append (Diccionario)

CrearDiccionario(TuplasLista)


# Hago un loop para que los destinos se hagan en forma de lista y solo salgan uno de cada uno y que no salgan repetidos
for dt in Diccionario_01:
    Destinatarios.append(dt ['Destino'])
Destinatarios = set (Destinatarios)

print("Los destinos son: " + str(Destinatarios))


# Por ultimo hago un for y dentro de ese for ponga la condicion if para que si se cumple imprima lo que se pide y de lo contrario imprimiria no hay destinos asi alla.
def PasajerosDestino(Destinosolicitado):
    H = False
    for Diccionario in Diccionario_01:
        if Diccionario['Destino'] == DestinoSolicitado.title():
            print("\n" + str(Diccionario))
            H = True

    if H == False:
        print("No hay pasajeros para este destino." "\n")

DestinoSolicitado = (input("Buscar pasajeros con destino a: "))
PasajerosDestino(DestinoSolicitado)


print("========================= Fin del programa =========================")



 
