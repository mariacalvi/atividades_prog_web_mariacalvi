# Peça ao usuário para digitar o preço de uma mercadoria, o desconto e o imposto e
# calcule o preço final da mercadoria. 

preco_mercadoria = float(input("Digite o preço da mercadoria(R$): "))
desconto = float(input("Digite o valor do desconto da mercadoria(R$): "))
imposto = float(input("Digite o valor do imposto da mercadoria(R$): "))

preco_final = (preco_mercadoria + desconto) - imposto
print(f"O preço final da mercadoria é R${preco_final}")