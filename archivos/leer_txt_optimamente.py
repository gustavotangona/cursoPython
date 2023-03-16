#abriendo el archivo con with Open
with open ("archivos\\texto_gustavo.txt") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    #mostramos el archivo
    print(contenido)
 # y no es neceasario cerrarlo si usamos WITH OPEN
    
    
