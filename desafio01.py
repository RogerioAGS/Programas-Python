# Desafio 01 - Cálculo do IMC
# Desenvolver um programa que calcule o IMC da pessoa:
# Requisitos:
# [ ] Peso e altura da pessoa será digitado pelo teclado (Dica: usar input() e 
# conveter usando o float() )
# Exemplo: 
# peso = input("Digite seu peso")
# peso = float(peso)
# ou
# peso = float(input("Digite seu peso"))
# [ ] A pessoa vai se identificar através do nome (Dica: usar input() ),
# [ ] Realizar o cálculo padrão do IMC (Dica: usar operadores aritmeticos e variaveis)
# [ ] Apresentar o resultado na tela com o Nome e o Valor do IMC (Dica: usar print() com 
#       formatação print(f"") e as variaveis entre {} )


# Exemplo de ajuste no número
# imc = 3.35555
# # Arredondamento
# print('IMC', round(imc,2) )
# # Coloca 2 casas após a virgula
# print('IMC %.2f' %imc)

print("--------- CALCULO DO IMC ---------")
nome = input("Olá, qual é seu nome:")

altura = float( input("Digite sua altura em metros: "))
peso = float( input("Digite seu peso em quilos: "))

imc = peso / (altura ** 2)
imc = round(imc,2)

print(f"{nome}, seu imc eh {imc}")
print(nome, " seu imc eh ", imc)