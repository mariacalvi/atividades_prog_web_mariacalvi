# Imprima a tabuada de um número digitado pelo usuário

numero = int(input("Digite um número: "))

for i in range(0, 11):
   resultado = numero * i
   print(f"{numero} x {i} = {resultado}")