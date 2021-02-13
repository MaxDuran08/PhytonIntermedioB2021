#Ejercicio 1

frutas={'platano':1.35,'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}

fruta= input("¿Que fruta quiere?").title()

kg=float(input("¿cuantos kilos?"))

if fruta in frutas:
    print(kg, " kilos de ", fruta," valen ",frutas[fruta]*kg)
else:
    print("la fruta ", fruta," no esta a la venta")


#Ejercicio 2

numero = int(input("Ingrese un numero de 1 a 10: "))
archivo=open("archivo.txt","w")
for i in range(11):
    #print(i)
    archivo.write(numero," * ",i," = ",numero*i,"\n")
archivo.close()