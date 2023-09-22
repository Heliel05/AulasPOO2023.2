fatorial = int(input("digite o número: "))
soma = 1

while fatorial > 0:
    soma *= fatorial
    fatorial -= 1
print(soma)