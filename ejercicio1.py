linea="que lindo dia es hoy"
palabras= linea.split()
texto={k:palabras.count(k)for k in list(set(palabras))}
print(texto)