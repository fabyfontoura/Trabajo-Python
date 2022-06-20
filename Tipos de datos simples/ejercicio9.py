cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("Interés porcentual anual? "))
años = int(input("¿años? "))
print("capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
                              
