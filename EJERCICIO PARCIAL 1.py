numeros = []
n = 10

for i in range(n):
    valor = int(input("Ingrese el valor: "))
    numeros.append(valor)

suma = sum(numeros)
promedio = suma / n
print("Promedio de la suma es:", promedio)

while promedio > 1:
    if promedio % 2 == 0:
        promedio = promedio / 2
    else:
        promedio = promedio * 3 + 1
    print(promedio)
