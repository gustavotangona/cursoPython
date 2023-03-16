#creando un conjunto con Set
conjunto = set(["dato1"])
print(conjunto)

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"} 
print(conjunto2)

#Teoria de conjuntos d
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto2)
print(resultado)
resultado = conjunto2 <= conjunto1
print(resultado)

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)

