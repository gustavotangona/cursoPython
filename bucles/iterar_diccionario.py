diccionario = {
    "nombre": "Gustavo",
    "apellido": "tangona",
    "dni": 27059198
}
# recorriendo diccionario con items obteniendo clave y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es : {value}')
    
    