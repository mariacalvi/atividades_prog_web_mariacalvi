# Peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de
# transição de uma para outra e calcule a aceleração.

velocidade_inical = float(input("Digite a velocidade inicial: "))
velocidade_final = float(input("Digite a velocidade final: "))
tempo_transicao = float(input("Digite o tempo de transição entre a velocidade inical e a velocidade final: "))

aceleracao = (velocidade_final - velocidade_inical) / tempo_transicao

print(f"A aceleração é {aceleracao}")