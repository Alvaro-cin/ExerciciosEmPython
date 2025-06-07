n1, n2, n3 , n4 = map(float, input("Digite as suas 4 notas  separadas por espaço: ").split())
if (n1+n2+n3+n4)/4 >= 50:
    print("Aprovado com media: ", (n1+n2+n3+n4)/4)
else:
    print("Reprovado com media: ", (n1+n2+n3+n4)/4)