# Desafio 09
# - Você deverá desenvolver um programa de votação 
# - Para realizar a votação o eleitor deverá digitar seu CPF e escolher
# o candidato pelo número [1, 2, 3]
# - Quando finalizar a votação seu programa deverá mostrar a quantidade
# de votos para cada candidato

lista_CPF = []
lista_votos = []

print("-------- ELEIÇÕES 2024 ---------")

continua = input("Deseja iniciar a votação (S/N)")

while continua == 'S' or continua == 's':

    cpf = input("Digite seu CPF: ")
    voto = int(input("Digite o número do candidato [1, 2, 3]: "))

    lista_CPF.append(cpf)
    lista_votos.append(voto)

    continua = input("Deseja continuar a votação (S/N)")

print("Quantidade de votos para o candidato 1", lista_votos.count(1))
print("Quantidade de votos para o candidato 2", lista_votos.count(2))
print("Quantidade de votos para o candidato 3", lista_votos.count(3))