#importando un modulo y asignandole el nombre m_saludar
#import modulo_saludar as m_saludar
from modulo_saludar import saludar,saludar_raro 
#desde ese modulo importamos 2 funciones
saludo= saludar("Gustavo")
saludo_raro=saludar_raro("Lorenzo")
#mostramos los resultados
print(saludo)
print(saludo_raro)


