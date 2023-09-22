num = int(("Digite um numéro de 1 a 10000: "))
cont = 0
for i in range(1,num + 1):
    if i % num == 0:
        cont += 1
if cont == 2:
    print("É primo!")
else:
    print("Não é primo!")
