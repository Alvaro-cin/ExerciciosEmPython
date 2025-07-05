print("Colocar 1 grão na 1ª casa, e dobrar a quantidade em cada casa seguinte, até completar as 64 casas do tabuleiro de xadrez.")
graos = 1
soma = 1 
for a in range(2,65):
    graos *= 2
    soma += graos
print(soma)
