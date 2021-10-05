edad = int (input("Digame la edad: "))
tipo_carnet = input("Tipo de carnet (Estudiante, Pensionista, Fam Num, Nada: ")

if 25 <= edad <= 35 and tipo_carnet == "E" or \
        edad < 10 or\
        (edad > 35 and tipo_carnet == "P") or \
        tipo_carnet == "F":
    print("Se te aplica el descuento")
else:
    print("No se aplica el descuento")