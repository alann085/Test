num = int(input("Digite um número:"))
inicio = 2
primo = True

while inicio < num:

    if num % inicio == 0:
        primo = False
        break
    inicio +=1

if primo == True:
    print("Ele é primo")
else:
    print("Ele não é primo")