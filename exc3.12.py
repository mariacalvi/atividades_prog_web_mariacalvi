# Soma todos os números primos de 1 a 100.
soma = 0

for i in range(2, 101): 
    e_primo = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            e_primo = False
            break

    if e_primo:
        soma += i

print(soma)
