'''
    MAX DURAN CANTEO


    Ejericio 1
'''


def discount(discount, price):
  return discount*price

def iva(price):
  return 0.12*price

def funcion3(dicc):
    finalPrice = 0
    for i in range(len(dicc['prices'])):
        diss = discount(dicc['discounts'][i],dicc['prices'][i])
        _iva = iva(dicc['prices'][i])
        finalPrice+=dicc['prices'][i] - diss + _iva
    return finalPrice
    


dictionary = {'prices':[100, 200, 300, 40,800], 'discounts':[0.1,0.2,0.03,0.05,0.06]}


print(funcion3(dictionary))


#Ejericio 2

def funcionHija(n):
    return n*n

def funcionPadre(funcion, arr):
    for i in range(len(arr)):
        arr[i] = funcion(arr[i])
    return arr

arreglo = [1,2,3,4]

print(funcionPadre(funcionHija, arreglo))