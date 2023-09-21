"""Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo."""

inter1 = int(input("Digite o primeiro número do intervalo: "))
inter2 = int(input("Digite o segundo número do intervalo: "))
valor = int(input("Digite o número para o teste: "))

if (valor >= inter1 and valor <= inter2):
    print("Valor dentro do intervalo!")
elif (valor <= inter1 and valor <= inter2):
    print("Valor fora do intervalo na parte inferior!")
else:
    print("Valor fora do intervalo na parte superior!")