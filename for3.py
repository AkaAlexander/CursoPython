texto_usuario = "Hola, me llamo Alex. ¿Tu como te llamas?"
espacios = 0
puntos= 0
comas = 0

for letra in texto_usuario:
    if letra == " ":
        espacios+=1
    elif letra == ".":
        puntos+=1
    elif letra == ",":
        comas+=1

print("espacios {}\npuntos {}\ncomas {}".format(espacios,puntos,comas))
