# Escreva um programa que verifique se uma string é um número real ou não (pode
# usar estrutura de repetição).

texto = input("Digite uma string para verificar se é ou não um número real: ")
real = True
tem_decimal = False

for caractere in texto:
    if caractere == '.':
        if tem_decimal:
            real = False
            break
        tem_decimal = True
    elif not caractere.isdigit():
        real = False
        break

if real:
    print("É um número real")
else:
    print("Não é um número real")
