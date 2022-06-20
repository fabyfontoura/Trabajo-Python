peso_payaso = 115
peso_muñeca = 69
payaso = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso + peso_muñeca * muñecas
print("El peso total del paquete es: " + str(peso_total))
