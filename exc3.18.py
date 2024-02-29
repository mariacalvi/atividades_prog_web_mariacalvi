# Imprimir a sequência de Fibonacci até o n-ésimo termo, onde n é digitado pelo
# usuário.

n = int(input("Digite a quantidade de termos da sequência: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_termo)

print(fibonacci)

