# 2 listas,una con nombres y otra con apellidos
nombres =["Lucas","Matias","Gustavo","Camila","Pedro"]
apellidos =["Tangona","Jose","Perez","Lopez","Gonzales"]

#Registrar esta info en un txt de forma optima
with open ("resolviendo_problemas\\nombres_y_apellidos.txt","w")as arch:
    arch.writelines("Los datos son:\n") 
    [arch.writelines(f"Nombre: {n}\n Apellido: {a}\n----------\n")for n,a in  zip(nombres,apellidos)]
