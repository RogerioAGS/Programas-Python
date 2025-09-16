# Variaveis -> espaço dentro da memoria RAM para guardar
# dados/informações

# Nomes das variáveis:
# - não podem começar com números: 1num = 20
# - não podem ter caracteres especiais: preço -> preco
# - não podem ter espaços: (valor carro), quando 
# necessário utilizar o _ (underscroll)
# valor_carro / valorCarro (camel Case)
# - colocar nomes significativos para as variaveis

# Variáveis do Tipo Número Inteiro (0, 1, 2, -9, 22222222)
idade = 32
numero_de_alunos = 15
numeroAlunos = 15
temperatura = -3

# Case Sensitive - Sensivel ao caso
python = 0
Python = 0
PYTHON = 0
pyTHON = 0

# Variáveis do Tipo Real (Números reias / Ponto Flutuante: 1.2,  7.98, 3.1415)
altura = 1.74
precoProduto = 19.99
largura = 15.0

# Variávies do Tipo Strings (Palavras, Frases, Letras, Caracteres)
# - devem estar entre aspas duplas ou simples
nome = "Alice"
mensagem = "Olá, seja bem-vindo!!!"
endereco = 'Rua das Flores, 123'

# Variáveis do Tipo Booleano (True ou False)
isPythonFun = True
hoje_esta_sol = False

print("A idade de Jose eh: ", idade)
print("Sua altura eh: ", altura)
print("Seu endereço eh:", endereco)
print("Hoje está ensolarado? ", hoje_esta_sol)

print(f"Ola {nome}! Voce te, {idade} anos.")
print("Ola", nome, "! Voce tem", idade, "anos.")