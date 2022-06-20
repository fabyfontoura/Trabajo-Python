edad = int(input("Introduce tu edad: "))
# " Decisión del precio en función de la edad
if edad < 8:
           precio = 100
elif edad <= 16:
    precio = 250
else:
    precio = 50
# Mostrar precio
print("El precio de la entrada es", precio, "$.")

           
