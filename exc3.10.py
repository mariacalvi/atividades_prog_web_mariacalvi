# Imprima todos os números primos de 1 a 100

for i in range(2, 101):
    primo = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            primo = False
            break

    if primo:
        print(i)
