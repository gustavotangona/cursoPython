# creando una funcion q nos devuelva los numeros primos 
# entre 0 y el numero que le pasamos

def es_primo(num):
    #verificamos q el numero solo pueda dividirse por si mismo y x 1
    for i in range(2,num-1):
        if num%i==0: return False
    return True
#creando una funcion q retorne una lista con todos los primos 
def primos_hasta(num):
    primos=[]
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos
            

resultado = primos_hasta(13)
print(resultado)