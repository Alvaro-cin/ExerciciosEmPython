soma=0
media = 0
for a in range(1,16):
      n1 = float(input(f" Digite o {a}° número: "))
      media += n1
      fatorial = 1
      for b in range(1,int(n1)+1):
          fatorial *= b
      soma += fatorial
print(f"O somatório da fatorial de cada valor e:{soma}  e a media e{media/15}")