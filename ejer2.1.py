cadenaPalabras = 'Generalmente se suele decir que la frase mas larga de la literatura se encuentra en En busca del tiempo perdido Tiene su logica en su celebre novela Proust puede detenerse decenas de paginas para describir los detalles mas triviales y cotidianos Pero claro depende de lo que entendamos por frase de si hacemos o no separacion por periodos de sentido completo o si tenemos en cuenta el punto y coma como pausa fuerte al mismo nivel que el punto Por eso no hay acuerdo unanime en cual de las largas frases de Proust es la mas larga '
cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))