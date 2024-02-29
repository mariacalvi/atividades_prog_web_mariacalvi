# Verifique se um número digitado pelo usuário é perfeito

numero = int(input("Digite um número: "))
soma = 1

for i in range(2, int(numero/2) + 1):
    if numero % i == 0:
        soma += i
    
if soma == numero: 
    print(f"{numero} é um numero perfeito")
else:
    print(f"{numero} não é um número perfeito")