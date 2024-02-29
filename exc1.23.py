# Peça ao usuário para digitar a distância percorrida, o tempo gasto e a aceleração
# de um objeto e calcule a velocidade inicial e final.

distancia_percorrida = float(input("Digite a distância percorrida pelo objeto(m): "))
tempo_gasto = float(input("Digite o tempo gasto(s): "))
aceleracao = float(input("Digite a aceleração do objeto (m/s): "))

velocidade_inicial = (distancia_percorrida / tempo_gasto) - ((aceleracao * tempo_gasto) / 2 )
velocidade_final = velocidade_inicial + (aceleracao * tempo_gasto)

print(f"A velocidade inicial é {velocidade_inicial} e a velocidade final é {velocidade_final}")