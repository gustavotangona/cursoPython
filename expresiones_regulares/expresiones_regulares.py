import re
texto = '''Hola maestro.esta es la cadena 1. como estas mi capitan
esta es la linea 2 de texto
esta es la linea 225 de texto.
y esta es la final (linea 3)definitiva mi capitan'''
         
#haciendo una busqueda simple
#resultado = re.search("Hola",texto)

#\d -- busca digitos numericos del 0 al 9--si la D es mayuscula devuelve todo menos los numeros
#resultado = re.findall(r"\d",texto)

#\w -- busca caracteres alfanumericos [a-z A-Z 0-9 _]---si es W es todo lo contrario
#resultado = re.findall(r"\w",texto)

#\s -- busca espacios en blanco,tabs o saltos de linea---si es S es todo lo contrario
#resultado = re.findall(r"\s",texto)

#armando una cadena que busque un punto,seguido de un texto y un espacio
#resultado = re.findall(r'\d\.\s',texto)

#buscando el principio de una linea
# \ʌ  -- busca el comienzo de una linea
resultado = re.findall(r'^esta',texto,flags=re.M)   #flags=re.M activa la mutilinea

# \$  -- busca el final de una linea
resultado = re.findall(r'capitan$',texto,flags=re.M)

#{n,m} ---> busca al menos n cantidad de veces, y como maximo M 
resultado = re.findall(r'\d{1,4}',texto)

print(resultado)  
