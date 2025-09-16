# Estrutura de Repetição (Loops) - Utilizada para repetir uma parte 
# do código ou percorrer listas(Arrays)

frutas = ["pera", "uva", "maçã", "banana", "melancia", "laranja", "abacaxi", "limão", "carambola"]

# print("1 - ", frutas[0])
# print("2 - ", frutas[1])

# FOR
# 1. Lista Inteira 
# for i in range(9):
#     print(i+1, "-", frutas[i])

# # 2. Intervalo entre os numeros 5 até o 15
# for i in range(5,16):
#     print(i)

# 3. Ajustando o tamanho da lista automaticamente 
# for i in range( len(frutas) ):
#     print(i+1, "-", frutas[i])

# 4. Listas - Mais comum
# for elemento in lista:
#   elemento

# for fruta in frutas:
#     print(fruta)


# WHILE
# Definir a condição, condição final e o incremento

# Condição Inicial
i = 0
#Condição Final
while i < 11:
    print(i)
    #Incremento
    i = i + 2

