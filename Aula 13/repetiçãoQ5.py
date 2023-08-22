import random

numero = random.randint(1,100)
tentativa = int(input("Tente advinhar um número de 1 a 100: "))

while tentativa != numero:

    if tentativa > numero:
        print("chute alto")
    else:
        print("chute baixo")

    tentativa = int(input("Tente de novo:"))

print("Você acertou, o número era", numero)