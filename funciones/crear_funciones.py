#creando una funcion simple
def saludar():
    print("Hola Lucas mi maestro,,Como Andas?")
#ejecuando la funcion simple    
saludar()

#crear una funcion con parametro
def saludar(nombre,sexo):
    sexo =sexo.lower()
    if (sexo == "mujer"):
        print(f'Hola{nombre} mi hermosa,como estas?')
    else:   
       print(f'Hola {nombre}mi maestro,como andas??')
    
saludar('Camila',"mujer")

#crear una funcion q nos retorne valores
def crear_contraseña(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contraseña)

password = crear_contraseña(8)
frase =f"Tu contraseña nueva es: {password}" 
print(frase)
    