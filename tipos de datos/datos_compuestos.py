#creando una lista
lista = ["Lucas Dalto","Gustavo Tangona",True,1.85]
print(lista)
print(lista[1])
lista[2]="programando"
print(lista[2])
#creando una tupla
tupla = ("Lucas Dalto","Gustavo Tangona",True,1.85)
print(tupla[2])
#creando un conjunto Set (no se puede llamar a un elemento x su indice y no almacena datos duplicados)
conjunto ={"Lucas Dalto","Gustavo Tangona",True,1.85,1.85}
print(conjunto)
#creando un diccionario ( seria el Json de Javascript)estructura: key:value
diccionario= {
    'nombre': "Lucas Dalto",
    'esta emocionado': True,
    'altura': 1.85 
}
print(diccionario)
print(diccionario['nombre'])