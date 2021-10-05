import random

adivina = random.randint(1,10)

numeroPersona = int(input("Dime un numero: "))

if numeroPersona > 10 or numeroPersona < 0:
    print("Te has pasado de los limites entre 0 y 10")

if numeroPersona == adivina:
    print("Enhorabuena as adivinado el numero")
else:
    print("Has fallado")

print("El numero ganador era {}".format(adivina))
