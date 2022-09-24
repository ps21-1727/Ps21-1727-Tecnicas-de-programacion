#Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. 
#Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias,
#I para industrias y C para comercios.
#Calcule el precio a pagar de acuerdo con la siguiente tabla:

tarifa_a_pagar = int(input("Cuantos kwh consumio? "))
instalacion = str(input("Que tipo de instalacion tiene? "))
r ="Residencial"
i ="Industria"
c ="Comercios"

#residencial
if tarifa_a_pagar <= 500:
    print("Usted es residencial y pagara RD$550 pesos dominicanos")
if tarifa_a_pagar >= 500:
    print("Usted es residencial y pagar RD$850 pesos dominicanos")
    
#comercial
if tarifa_a_pagar <= 1000:
    print("Usted es comercial y pagara RD$1300 pesos dominicanos")
if tarifa_a_pagar > 1000:
    print("Usted es comercial y pagara RD$2500 pesos dominicanos")

#industrial
if tarifa_a_pagar <= 5000:
    print("Usted es industrial y pagara RD$3800 pesos dominicanos")
if tarifa_a_pagar > 5000:
    print("Usted es industrial y pagara RD$4200 pesos dominicanos")
