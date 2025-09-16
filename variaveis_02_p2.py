# Métodos das listas
# - funções para modificar as listas,

frutas = ["pera", "limao", "abacate", "limao"]

# print("Original:")
# print(frutas)

# Append - incluir um elemento no final da lista
frutas.append("laranja")

# Insert - incluir um elemento em uma posicao determinda da lista
frutas.insert(0,"uva")

# Remove - remover o 1º elementa encontrado na lista
frutas.remove("limao")

# Pop - retira um elemento da lista e guarda em uma variavel
elemento = frutas.pop(2)

# Sort - organizar a lista em ordem crescente
frutas.sort()

# Reverse - inverter a lista
frutas.reverse()

# Count - conta quantos elementos do tipo especificado tem na lista
num_limoes = frutas.count("limao")
# print(num_limoes)

# print("Modificada:")
# print(frutas)
# print(elemento)

cadastro = {
    "nome"      :   "Jairo",
    "sobrenome" :   "Candido",
    "endereco"  :   "Rua Luis Lacava",
    "cidade"    :   "Maua",
    "estado"    :   "São Paulo"
}

# print(cadastro)
# print( cadastro.keys() )
# print( cadastro.values() )

# valor = cadastro.get("nome")
# print(valor)

print(cadastro)
cadastro.clear()
print(cadastro)

