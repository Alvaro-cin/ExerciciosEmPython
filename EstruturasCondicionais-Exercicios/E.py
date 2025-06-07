import math
a , b , c = map(float, input("Digite a b  e c separadas por espaço: ").split())
delta = b**2 - 4*a*c
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)
print(f"As raízes são: x1 = {x1:.2f} e x2 = {x2:.2f}") 
if delta < 0 :
    print("Não há solução real")
elif delta > 0 :
     print("Há duas soluções reais e diferentes ")
elif delta==0 :
     print("Há apenas uma solução real")

     
   