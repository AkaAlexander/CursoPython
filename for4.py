import string

texto_usuario = input("Interoduzca un texto: ")
letas_mayusculas=0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letas_mayusculas+=1

print(letas_mayusculas)