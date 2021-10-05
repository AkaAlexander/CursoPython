lista_compra = []
input_usuario = None

print("Programa lista compra")

while input_usuario != "Q":
    input_usuario = input("¿Que desea comprar [Q] para salir?")
    if input_usuario == "Q":
        pass
    elif input_usuario in lista_compra:
        print("{} está en la lista de la compra".format(input_usuario))
    else:
        if input("Seguro que quiere añadir {} a la lista?[S/N]".format(input_usuario)) == "S":
            lista_compra.append(input_usuario)

print("La lista de la compra es:")
print(lista_compra)



