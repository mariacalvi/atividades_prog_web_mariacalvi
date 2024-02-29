# Escreva um programa que verifique se uma string é um número inteiro ou não e
# mostre uma mensagem de acordo (pode usar estrutura de repetição). 

texto = "12345"
NUMEROS = "0123456789"
eh_inteiro = True

for caractere in texto:
    if caractere not in NUMEROS:
        eh_inteiro = False
        break
if eh_inteiro:
    print("É um número inteiro!")
else:
    print ("Não é um numero inteiro")