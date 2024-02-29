# Peça ao usuário para digitar o valor inicial de um investimento, a taxa de juros e o
# número de anos e calcule o valor final do investimento considerando juros compostos. 

valor_inicial_investimento = float(input("Digite o valor inicial do investimento: "))
taxa_de_juros = float(input("Digite a taxa de juros(%): "))
anos = int(input("Digite o número de anos: "))

juros = taxa_de_juros / 100

valor_final_investimento = valor_inicial_investimento * (1 + juros)**anos

print(f"O valor final do investimento será {valor_final_investimento}")