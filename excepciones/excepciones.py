#creando funcion q suma numeros
def sumar_dos():
    # iniciando un bucle
    while True:
        #pidiendo numeros
        a= input("Numero 1 : ")
        b= input("Numero 2 : ")
        #convertimos esos numeros a ennteros y los sumamos
        try:
           resultado = int(a) + int(b)
           #si lanzo una excepcion pedimos q reingrese los datos
        except:
          print("Te pedi un nunmero no un texto")
        else:
            break
          #finally se ejecuta siempre
        finally:
            print("esto se ejecuta siempre")
    return resultado
#mostrando el resultado
print(sumar_dos()) 