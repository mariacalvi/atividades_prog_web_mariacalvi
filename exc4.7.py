# Crie um programa que peça ao usuário para digitar um nome de usuário e uma senha
# contendo apenas caracteres alfanuméricos e use expressão regular para fazer uma limpeza nos
# valores digitados, exibindo-os novamente para o usuário os valores que forem modificado
import re

usuario = input("Digite um nome de usuário: ")
senha = str(input(" Digite uma senha com caracteres alfanúmericos: "))

senha_modificada = re.sub('[A-Za-z0-9]', ' ',senha)
print(f"A senha sem caracteres alfanuméricos é: {senha_modificada}")