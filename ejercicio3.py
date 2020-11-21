
lista = []
 
salir = False
 
while(not salir):
    numero = int(input("INGRESE EL NUMERO: "))
    if(numero == 0):
        salir=True
    else:
        lista.append(numero)
 
lista.sort() 
 
print(lista)
