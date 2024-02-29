# Escreva um programa que verifique se uma pessoa é elegível para aposentadoria
# (se tem 60 anos ou mais para mulheres e 65 anos ou mais para homens).
genero = "homem"
idade = 60

if genero == "mulher" and idade >= 60 :
    print("É elegível para a aposentadoria !")
elif genero == "mulher" and idade < 60 :
    print("Não é elegível a aposentadoria.")
elif genero == "homem" and idade >= 65 :
    print("É elegível para a aposentadoria !")
else:
    print("Não é elegível para a aposentadoria.")