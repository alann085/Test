lista = []
quantidade = int(input("Digite a quantidade de itens: "))
for i in range (quantidade):
    item = input ("digite um item: ")
    lista.append (item)
    i +=1
lista.sort()
print(lista)