# Crie um programa que peça ao usuário para inserir dois números e calcule a potência
# do primeiro número pelo segundo número.
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: ")) 

potencia = primeiro_numero ** segundo_numero  
print(f"A potência do número {primeiro_numero} pelo número {segundo_numero} equivale a {potencia}")
## print(pow(a, b))