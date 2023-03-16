#usando open para abrir un archivo
archivo_sin_leer = open("archivos\\texto_gustavo.txt")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea x linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline(20)
print(linea)

#cerrar el archivo
archivo_sin_leer.close()
