numero_usuario = int(input("Introduce un numero para saber su tabla de multiplicar"))


for n in range (1,11):
    if n % 2 == 0:
        print("{} x {} = {}".format(n,numero_usuario,n*numero_usuario))




