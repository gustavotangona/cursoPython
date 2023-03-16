diccionario = {
    "nombre": 'Gustavo',
    "apellido": 'Tangona',
    "subs": '1000000'
}
# KEYS nos devuelve todas las keys del diccionario(tambien sirve para iterar)
claves = diccionario.keys()
print(claves)

#GET devuelve el valor de una clave del diccionario
claves = diccionario.get("apellido")
print(claves)

#CLEAR elimina todos los elementos del diccionario 

#POP elimina un elemento del diccionario
diccionario.pop("apellido")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
