# Crie um programa que peça ao usuário para digitar uma frase, uma palavra presente
# na frase e outra palavra ausente na frase. Em seguida, substitua todas as ocorrências da palavra
# existente pela palavra inexistente.

frase = input("Digite uma frase: ")
palavra_presente = input("Digite uma palavra na frase digitada: ")
palavra_ausente = input("Digite uma palavra que não está presente na frase acima: ")

nova_frase = frase.replace(palavra_presente, palavra_ausente)
print(nova_frase)