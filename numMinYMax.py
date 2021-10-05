""""
numeros = []


for n in range (1,6):
    num_usuario = int(input("Introduce numeros:"))
    numeros.append(num_usuario)

print("El numero mas pequeño es: {}\nEl número maximo es: {}".format(min(numeros),max(numeros)))

"""

numeros_introducidos = input("Introduzca los numeros separados por coma: ")

#List comprenhesion/Comprension de lista
numeros_usuario = [int(numero)for numero in numeros_introducidos.split(",")]

print(numeros_usuario)

numero_min =numeros_usuario[0]
numero_max = numeros_usuario[0]

for numero in numeros_usuario[1:]:
    if numero_min > numero:
        numero_min = numero

    if numero_max < numero:
        numero_max = numero

print("Numero grande {}, Numero pequeño {}".format(numero_max,numero_min))