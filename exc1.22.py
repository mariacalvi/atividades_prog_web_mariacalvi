# Peça ao usuário para digitar a distância percorrida por um objeto e o tempo gasto e
# calcule a velocidade média do objeto.

distancia_percorrida = float(input("Digite a distância percorrida pelo objeto(m): "))
tempo = float(input("Digite o tempo gasto pelo objeto(s): "))

velocidade_media = distancia_percorrida / tempo

print(f"A velocidade média do objeto é de {velocidade_media} m/s")