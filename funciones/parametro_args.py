def suma(a,b):
    return a+b

resultado = suma(5,3)
print(resultado)

#utilizando el parametro args
def suma(*numeros):
    return sum(numeros)
resultado = suma(4,5,6,7,8)
print(resultado)

    