# Peça ao usuário para digitar o nome, o preço de custo, o preço de venda e a quantidade
# em estoque de determinado produto e mostre o lucro que esse estoque pode gerar se todos os
# produtos forem vendidos

nome_produto = (input("Digite o nome do produto:"))
preco_custo_produto = float(input("Digite o preço de custo do produto:"))
preco_venda_produto = float(input("Digite o preço de venda do produto:"))
quantidade_produto = int(input("Digite a quantidade em estoque do produto:"))

lucro = ( preco_venda_produto - preco_custo_produto) * quantidade_produto
print (f"O lucro que esse estoque pode gerar é de {lucro}")