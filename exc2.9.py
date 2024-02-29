# Escreva um programa que verifique se uma string digitada pelo usuário é uma data
# no formato mm/dd/aaaa ou não.

data = input("Digite uma data (mm/dd/aaaa): ")

if len(data) == 10 and data[2] == '/' and data[5] == '/':
    if data[:2].isdigit() and data[3:5].isdigit() and data[6:].isdigit():
        mes, dia, ano = map(int, data.split('/'))


        if 1 <= mes <= 12 and 1 <= dia <= 31 and 1900 <= ano <= 9999:
            print("É uma data no formato mm/dd/aaaa.")
else:
    print("Não é uma data no formato mm/dd/aaaa.")
