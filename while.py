respuesta = None

while respuesta != "A" and respuesta !="B" and respuesta != "C":
    respuesta = input("Elige opcion A B C")

if respuesta == "A":
    print("Has elegido bien")
elif respuesta == "B":
    print("Podrias haber elegido mejor")
elif respuesta == "C":
    print("Elegiste mal")