numeros = []
#n = 7+ 3
n= 10
for i in range(n):
    valor = int(input("Ingrese el valor: "))
    numeros.append(valor)
for i in range (n):
    suma = sum(numeros)
    promedio =int( suma/n)
print("promedio de la suma es : ", promedio)

while promedio != 1:
    if promedio % 2 == 0:
        promedio= promedio/2
        print(promedio)
    else:
        promedio=promedio*3 +1
print(promedio)
    
