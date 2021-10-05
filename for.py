a = [1,2,3,4,5,6,7,8,9,10]

for item in a:
    print(item)

lista_compra = ["Leche","Arroz","Jamon"]

for item in lista_compra:
    print("Hoy voy a comprar {}".format(item))

vocales = ["a","e","i","o","u","A","E","I","O","U"]

frase = "Hola me llamo Alex"
vocales_encontradas=0
for letra in frase:
    print(letra)

for letra in frase:
    if letra in vocales:
        print("He encontrado una {}".format(letra))
        vocales_encontradas+=1
print ("Vocales encontradas: {}".format(vocales_encontradas))
