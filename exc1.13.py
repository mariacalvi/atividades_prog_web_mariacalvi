# Peça ao usuário para digitar três números e imprima a soma deles.

largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

area = largura * altura
perimetro = (2*largura) + (2*altura)

print (f"A área do retângulo é {area} e seu perímetro é {perimetro}")