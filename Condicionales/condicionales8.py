bonificacion = 3000
inaceptable = 0
aceptable = 0.6
meritorio = 0.8
puntos = float(input("Introduce tu puntuación: "))
# Clasificación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.8:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f$" % (puntos * bonificacion))
    
