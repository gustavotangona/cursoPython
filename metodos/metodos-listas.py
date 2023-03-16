# funcion List ---Crea una lista 
lista = list([55,66,34,77,44])
print(lista)

#LEN longitud de la lista,,,cantidad de elementos
resultado = len(lista)
print(resultado)

#APPEND agrega elemento a la lista ---
agregando_con_append = lista.append(99)
print(agregando_con_append)

#INSERT agregando elemento a la lista en un lugar especifico ---
lista.insert(2,88)
print(lista)

#EXTEND agrega varios elementos a la lista ---
lista.extend([False,2030])
print(lista)

#POP elimina un elemento x su indice---lista.pop(-1)elimina el ultimo elemento
lista.pop(0)
print(lista)

#REMOVE remueve un elemento de la lista x su valor
lista.remove(False)
print(lista)

#CLEAR elimina todos lo elementos de la lista--chau lista

#SORT ordena los elementos de manera ascendente
lista.sort()
print(lista)
