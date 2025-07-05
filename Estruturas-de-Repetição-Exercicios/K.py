soma=0
for a in range(1,16):
      n1 = int(input(f" Digite o {a}° número: "))
      fatorial = 1
      for b in range(1,n1+1):
          fatorial *= b
      soma += fatorial
print(f"O somatório da fatorial de cada valor e:{soma} ")