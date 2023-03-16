cadena1="hola,aala,12345"
cadena2="bienvenido maquinola"

#convierte a mayusculas
resultado = cadena1.upper()
print(resultado) 
#convierte a minusculas
resultado = cadena1.lower()
print(resultado) 
#convierte la primera letra a mayuscula
resultado = cadena1.capitalize()

print(resultado) 

#buscamos una cadena en otra cadena, si no encuentra nada devuelve -1
busqueda_find = cadena1.find("s")
print(busqueda_find)

#busqueda con index---busca una cadena en otra cadena tambien--si no encuentra devuelve una excepcion
busqueda_index=cadena1.index("l")
print(busqueda_index)

#is numeric ( si es numerico devuelve true,sino devuelve False)
es_numerico = cadena1.isnumeric()
print(es_numerico)

#si es alfa-numerico devuelve true,sino devuelve False)
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

# buscamos una cadena en otra cadena, contamos las veces q hay coincidencia
contar_coincidencias = cadena1.count("la")
print(contar_coincidencias)

#contamos la cantidad de caracteres de una cadena 
contar_caracteres = len(cadena1)
print(contar_caracteres)

# verificamos si una cadena empieza con una letra dada...o una cadena dadaa
empieza_con = cadena1.startswith("h")
print(empieza_con)

# reemplaza una parte de la cadena dada con otra cadena dada 
cadena_nueva = cadena1.replace("laaa","l")
 
print(cadena_nueva) 

#separa la cadena con la cadena q le pasemos
cadena_separada = cadena1.split(",")
print(type(cadena_separada))
print(cadena_separada[1])