numeros = [1,2,3,4,5,6,7,8,9,11,12,13,14,20]

#creando una funcion lambda para multiplicar x 2
mult_x_dos = lambda x : x*2

#creando una funcion que diga si es par o no
# def es_par(num):
#      if (num%2==0):
#           return True

# usando Filter con una funcion comun
# numeros_pares = filter(es_par,numeros)

#haciendo lo mismo q antes pero con Lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros) 
print((list(numeros_pares)))
