print("Aqui está o somatório dos valores pares de 1 a 500: ")
b = 0
for a in range(1,501):
    if a % 2 == 0:
        b += a
print(b)