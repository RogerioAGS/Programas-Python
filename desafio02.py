# Desafio 02
# Desenvolver um programa para uma loja de lanches (MAC)
# Requisitos:
# [ ] O usuário vai receber uma mensagem de boas vindas
# [ ] O sistema irá pedir qual seria a opção de lanche (Nº1, ...)
# [ ] O sistema irá retornar o nome lanche e o valor dele
# [ ] Usar pelo menos 4 opções de lanche
# [ ] Para resolver usar LISTAS 


# lista_lanches = ["Big Mac", "Quarteirao", "MC Chedder", "Big Tasty"]
# lista_precos = [19.99, 14.99, 24.99, 39.99]

# print("Olá, seja bem-vindo ao MAC SENAI Mauá")

# opcao = int( input("Digite o numero do lanche escolhido (1 à 4):") )

# print("Voce escolheu o lanche: ", lista_lanches[opcao-1])
# print("O valor do seu lanche é ", lista_precos[opcao-1])

lanches = {
    "1": ["Big Mac", "R$29.99"],
    "2": ["MAC Cheddar", "R$32.20"],
    "3": ["Quateirao", "R$19.20"],
    "4": ["Big Tasty", "R$49.20"],
}

print("Olá, seja bem-vindo ao MAC SENAI Mauá")
opcao = input("Digite o numero do lanche escolhido (1 à 4):")

print(f"O lanche que você escolheu eh {lanches[opcao][0]} e o valor eh {lanches[opcao][1]}")