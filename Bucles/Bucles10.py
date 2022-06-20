n = int(input("Introsduce un numero entero positivo mayor a 4: "))
i = 4
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
    
    
