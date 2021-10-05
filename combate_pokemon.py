from random import randint

VIDA_PIKACHU_INICIAL = 80
VIDA_SQUIRTLE_INICIAL = 90

TAMANIO_BARRA_VIDA = 20

vida_pikachu = VIDA_PIKACHU_INICIAL
vida_squirtle = VIDA_SQUIRTLE_INICIAL

while vida_squirtle>0 and vida_pikachu>0:
    # turnos de combate

    #turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        #bola voltio
        print("Pikachu ataca con Bola voltio")
        vida_squirtle-=10
    else:
        print("Pikachu ataca con Onda trueno")
        vida_squirtle-=11

    print("La vida de Pikachu es: {}, la de squirtle es {} ".format(vida_pikachu,vida_squirtle))


    #BARRAS DE VIDA
    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_PIKACHU_INICIAL)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_PIKACHU_INICIAL))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_SQUIRTLE_INICIAL)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_SQUIRTLE_INICIAL))


    input ("Enter para continuar....\n\n")

    #turno Squirtle
    print("Turno de Squirtle")
    ataque_squirtle=None
    while ataque_squirtle != "A" and ataque_squirtle !="P" and ataque_squirtle != "B":
        ataque_squirtle = input("¿Que ataque haces? Placaje, Pistola Agua, Burbuja ")

    if ataque_squirtle == "P":
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        vida_pikachu -= 9

    print("La vida de Squirtle es: {}, la de pikachu es: {} ".format(vida_squirtle,vida_pikachu))

    # BARRAS DE VIDA
    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_PIKACHU_INICIAL)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_PIKACHU_INICIAL))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_SQUIRTLE_INICIAL)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                              vida_squirtle, VIDA_SQUIRTLE_INICIAL))




    input("Enter para continuar....\n\n")

if vida_pikachu > vida_squirtle:
    print("PIKACHU GANA")
else :
    print("SQUIRTLE GANA")