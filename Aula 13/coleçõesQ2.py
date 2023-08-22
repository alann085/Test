lista = []
for i in range (5):
    num = input ("digite um número: ")
    lista.append (num)
    i +=1
lista.sort(reverse=True)
print(lista)