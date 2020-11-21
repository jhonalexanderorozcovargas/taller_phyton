def imc (estatura, peso):

    
    return peso / estatura**2   

peso = float(input("escriba su peso:"))
estatura= float(input("escriba su altura:"))

indice = imc(estatura, peso)

print ('su indice  es : {}'.format(indice))