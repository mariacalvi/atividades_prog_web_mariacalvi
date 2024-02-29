#  Crie um programa que peça ao usuário para inserir dois números complexos e calcule
# a soma e o produto desses números.
p_real = float(input("Digite a parte real do primeiro número complexo: "))
p_imaginaria = float(input("Digite a parte imaginária do primeiro número complexo: "))
s_real = float(input("Digite a parte real do segundo número complexo: "))
s_imaginaria = float(input("Digite a parte imaginária do segundo número complexo: "))

a = complex(p_real, p_imaginaria)
b = complex(s_real, s_imaginaria)

soma = a + b
produto = a * b

print (f"Soma: {soma}")
print(f"Produto: {produto}")
