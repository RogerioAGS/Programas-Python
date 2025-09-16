# Desafio 07
# - Faça um programa que cadastre as notas dos estudantes em um sistema
# - O programa deverá receber o nome e a nota dos estudantes pelo 
# teclado e guardar em listas
# - O programa irá parar somente quando a pessoa que tiver realizando o 
# cadastro finalizar
# - No final apresentar a lista de estudantes

lista_nomes = []
lista_notas = []

print("----------> Cadastro de Notas dos Estudantes <----------")

continua = 's'

while continua == 's':

    nome = input("Digite o nome do aluno: ")
    nota = input("Digite a nota do aluno: ")

    lista_nomes.append(nome)
    lista_notas.append(nota)

    continua = input("Deseja cadastrar um aluno (S/N) ")
    continua = continua.lower()

for i in range( len(lista_nomes) ):
    print(f"{i+1} - {lista_nomes[i]} \t - {lista_notas[i]}")
