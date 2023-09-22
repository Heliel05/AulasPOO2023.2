quant = int(input("Quantos usuários irão responder o questionario? "))
insa = 0
satis = 0
naoquero = 0
for i in range(quant):
    pesq = input("Qual o grau de satisfação com a farmácia? (INSATISFEITO; SATISFEITO; NÃO QUERO RESPONDER)")
    if pesq == "INSATISFEITO":
        insa += 1
    elif pesq == "SATISFEITO":
        satis += 1
    elif pesq == "NÃO QUERO RESPONDER":
        naoquero += 1
    else:
        print("Não é válido!")
print("Houveram ",(satis * 100),"%""de insatisfeitos!")
print("Houveram ",insa * 100,"% de satisfeitos!")
print("Houveram ",naoquero * 100,"% de Não quero responder!")