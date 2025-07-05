print("Sequência de fibonacci")
anterior = 0
depois = 1
for a in range(0,16):
    proximo = anterior + depois
    print(proximo)
    anterior = depois
    depois = proximo
