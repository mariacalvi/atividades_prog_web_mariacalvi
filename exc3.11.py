# Soma todos os números divisíveis por 3 ou 5 de 1 a 100
soma = 0

for i in range (1, 101):
    if i % 3 == 0 or i % 5 == 0 :
        soma += i

print(soma)