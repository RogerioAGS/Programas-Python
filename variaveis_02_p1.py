# Variável do Tipo Lista (Mutável/Pode ser modificada)
# a lista utiliza o colchetes para definir seus elementos
lista_de_frutas = ["pera", "banana", "uva", "mamao"]


# Variável do Tipo Tupla (Imutável/NÃO pode ser alterada )
# a tupla utiliza o parenteses para definir seus elementos
tupla_de_cores = ("vermelho", "azul", "verde", "preto")

# # Exibir os valores das variáveis
# print("Minha lista de frutas: ", lista_de_frutas)
# print("Tupla de cores: ", tupla_de_cores)

# # Acessa elementos especificos
# # Lista e Tupla sempre o primeiro indice é zero
# print("A segunda fruta da minha lista eh ", lista_de_frutas[1])
# print("O segundo elemento da minha tupla eh ", tupla_de_cores[1])

# carros = ["Etios", "Uno", "Mobi", "Up", "Palio", "Onix"]
# print(carros)
# print(carros[2])
# print(carros[5])
# print(carros[-1])
# print(carros[1:4])
# print(carros[:2:-1])

# Variável do Tipo Dicionário
# - o dicionário utliza chaves para definir seus elementos
# - o dicionário não tem indice - trabalha com chave e valor (key/value)
dicionario_de_pessoa = {
    "nome"  :   "Alice",
    "idade" :   25,
    "cidade":   "Mauá",
    "cpf"   :   12345678910
}

# Exibir os valor do dicionario
print("Dicionario de pessoas: ", dicionario_de_pessoa)

# Acessar valores especificos pelas chaves
print(f"A idade de {dicionario_de_pessoa['nome']} eh {dicionario_de_pessoa['idade']}")