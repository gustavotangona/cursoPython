# iterando lista con For In
animales =  ["gato","perro","loro","cocodrilo"]
numeros = [10,62,12,70]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a : {animal}')

#recorriendo la lista numeros y haciendo una pequeña operacion    
for numero in  numeros:
    resultado = numero * 10
    print(resultado)
    
#recorriendo las 2 listas simultaneamente
for numero,animal in zip(animales, numeros):
    print(f'Recorriendo la lista 1 : {numero}')
    print(f'Recorriendo la lista 2 : {animal}')

#itera e imprime los numeros desde 5 hasta 10    
for num in range(5,10):
    print(num)
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es :{indice} y el valor es:{valor}')
    
# usando el else en el For
for numero in numeros:
    print(f'ejecutando el ultimo bucle,valor actual: {numero}' )
else:
    print('el bucle termino')
    
    
    
    
    
    