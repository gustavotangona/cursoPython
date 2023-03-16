frutas = ["banana","manzana","pera","ciruela","naranja","granada"]
cadena = "hola gustavo"
numeros = [2,3,5,7,9]
# evitando que se coma la granada con la sentencia CONTINUE
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'Me voya comer una {fruta}')
    
    #evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f'Me voya comer una {fruta}')
    if fruta == 'pera':
      break
    print(f'Me voya comer una {fruta}')   
print("bucle terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

    
    

        