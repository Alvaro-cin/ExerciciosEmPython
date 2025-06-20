print("Bem vindo a calculadora simples")
n1 = float(input("Digite o Primeiro Valor: "))
n2 = float(input("Digite o Segundo Valor: "))
op = str(input("Que operacao quer realizar? ( + , - , / , * ) "))
if op == '-':
    print(n1 , " - ",n2 ,"e " , n1-n2)
elif op == '+':
     print(n1 , " + ",n2 ,"e " , n1+n2)
elif op == '/':
      print(n1 , " / ",n2 ,"e " , n1/n2)
elif op == '*':
      print(n1 , " * ",n2 ,"e " , n1*n2)
      print