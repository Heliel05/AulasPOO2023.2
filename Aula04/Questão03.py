temp = int(input("Qual a temperatura? "))
if temp < 15:
    print("Aqui não é o RN!")
elif temp > 15 and temp <= 25:
    print("Pense num frio!")
elif temp >= 26 and temp <= 30:
    print("Temperatura normal e super agradável!")
elif temp >= 31 and temp <= 35:
    print("Tá quente pra danado!")
elif temp > 35:
    print("Calor da muléstia!")