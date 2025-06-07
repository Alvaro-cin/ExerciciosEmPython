n1, n2, n3 , n4 = map(float, input("Digite as suas 4 notas  separadas por espaço: ").split())
md1 = (n1+ n2+ n3 + n4)/4
if md1 >= 70:
    print("Aprovado!")
else:
    ne = float(input("Me informe a nota do exame: "))
    if (md1+ne)/2 >= 50:
        print("Aprovado!")
    else:
        print("Reprovado!")