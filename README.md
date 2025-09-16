Agenda SQLite

import sql_funcoes as sf

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Atualizar Registro")
    print("3 - Apagar Registro")
    print("4 - Consultar Todos os Registro")
    print("5 - Consultar os Registros pelo Inicio e Quantidade")
    print("6 - Sair")

def menuInserir(bd):
    os.system("cls")
    print("-------> MENU INSERIR DADOS <-------")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    email = input("Digite o email: ")

    sf.inserirDados(bd, nome, sobrenome, email)

def menuAtualizar(bd):
    os.system("cls")
    print("-------> MENU ATUALIZAR DADOS <-------")
    print("Digite os dados para atualizar ou enter para continuar")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    email = input("Digite o email: ")
    num_registro = input("Digite o numero do registro para atualizar: ")

    sf.atualizarDados(bd, nome, sobrenome, email, num_registro)

def menuApagar(bd):
    os.system("cls")
    print("-------> MENU APAGAR DADO <-------")
    num_registro = input("Digite o numero do registro para apagar: ")

    os.system("cls")
    confirmar = int(input(f"DESEJA REALMENTE APAGAR O REGISTRO {num_registro}? DIGITE 1 PARA CONFIRMAR: "))

    if confirmar == 1:
        sf.apagarDado(bd, num_registro)
        print("Registro Apagado com Sucesso!!!!")
    else:
        print("Operacao CANCELADA!!!")

    os.system("pause")

def menuSelecionarTodos(bd):
    os.system("cls")
    print("-------> MENU SELECIONAR TODOS OS DADOS <-------")

    lista_dados = sf.selecionarTodosDados(bd)

    qtd_registros = int(input("Digite a quantidade de resitros por pagina: "))
    num_registros = 1

    print(f"ID\t\tNOME\t\tSOBRENOME\t\tEMAIL\n")
    for dado in lista_dados:
        print(f"{dado[0]}\t\t{dado[1]}\t\t{dado[2]}\t\t\t{dado[3]}\n")

        if num_registros >= (qtd_registros):
            os.system("pause")
            num_registros = 0

        num_registros += 1    

    os.system("pause")

def menuSelecionarParcial(bd):
    os.system("cls")
    print("-------> MENU SELECIONAR DADOS PARCIAL <-------")

    quantidade = input("Digite a quantide de registros para visualizar: ")
    inicio = input("Digite o numero do primeiro registro: ")

    lista_dados = sf.selecionarDadosParcial(bd, quantidade, inicio)

    print(f"ID\t\tNOME\t\tSOBRENOME\t\tEMAIL\n")
    for dado in lista_dados:
        print(f"{dado[0]}\t\t{dado[1]}\t\t{dado[2]}\t\t\t{dado[3]}\n")   

    os.system("pause")


def main():

    bd = "agenda.db"

    sf.criarTabela(bd)

    opcao = 0

    while opcao != 6:

        menuPrincipal()
        opcao = int(input("Digite uma opcao: "))

        if opcao == 1:
            menuInserir(bd)
        elif  opcao == 2:
            menuAtualizar(bd)
        elif  opcao == 3:
            menuApagar(bd)
        elif  opcao == 4:
            menuSelecionarTodos(bd)
        elif  opcao == 5:
            menuSelecionarParcial(bd)
        elif  opcao == 6:
            os.system("cls")
            print("Programa Finalizado....")
        else:
            os.system("cls")
            print("Opcao Invalida!!!")
            os.system("pause")

        os.system("pause")


if __name__ == "__main__":
    main()

arquivo app1

# Nome: Ana	Salario: 5000	Imposto: 1500.0
# Nome: Joao	Salario: 2300	Imposto: 690.0
# Nome: Bia	Salario: 6200	Imposto: 1860.0
# Nome: Jose	Salario: 9000	Imposto: 2700.0
# Nome: Paulo	Salario: 1560	Imposto: 468.0
# Nome: Lara	Salario: 11220	Imposto: 3366.0

def main():

    pessoas = ["Ana", "Joao", "Bia", "Jose", "Paulo", "Lara"]
    salarios = [5000, 2300, 6200, 9000, 1560, 11220]

    arquivo = open("registro.txt", "w+")

    for i in range ( len(pessoas) ):
        arquivo.write("Nome: ")
        arquivo.write(pessoas[i])
        arquivo.write("\tSalario: ")
        arquivo.write( str(salarios[i]) )
        arquivo.write("\tImposto: ")
        arquivo.write( str (salarios[i]*0.3) )
        arquivo.write("\n")

        # arquivo.write(f"Nome: {pessoas[i]}\tSalario: {salarios[i]}\tImposto: {str(salarios[i]*0.3)} \n") 

    arquivo.close()


if __name__ == "__main__":
    main()

Arquivo app2

def main():

    pessoas = ["Ana", "Joao", "Bia", "Jose", "Paulo", "Lara"]
    salarios = [5000, 2300, 6200, 9000, 1560, 11220]

    arquivo = open("registro.csv", "w+")

    # Arquivo CSV -> Excel
    # Nome das Colunas
    arquivo.write("Nome;Salario;Imposto\n")
    for i in range ( len(pessoas) ):
        arquivo.write(pessoas[i])
        arquivo.write(";")
        arquivo.write( str(salarios[i]) )
        arquivo.write(";")
        arquivo.write( str (salarios[i]*0.3) )
        arquivo.write("\n")

        # arquivo.write(f"{pessoas[i]};{str(salarios[i])};{str (salarios[i]*0.3)}\n")

    arquivo.close()


if __name__ == "__main__":
    main()

Arquivo app3

# Desafio
# Programa para registrar pessoas em um sistema que vai gravar um 
# arquivo no disco
# O programa irá registrar o nome, sobrenome, idade, cidade, estado
# Será feito um arquivo por um lote de 5 registros

def main():
    nomes = []
    sobrenomes = []
    idades = []
    cidades = []
    estados = []

    cadastrar = 's'

    while (cadastrar == 's' or cadastrar == 'S') and (len(nomes) < 5):

        # nome = input("Digite seu nome: ")
        # nomes.append(nome)

        nomes.append(input("Digite seu nome: "))     
        sobrenomes.append(input("Digite seu sobrenome: ")) 
        idades.append(input("Digite sua idade: "))  
        cidades.append(input("Digite sua cidade: ")) 
        estados.append(input("Digite seu estado: "))   


        cadastrar = input("Deseja realizar um novo cadatro (S ou s)")

    arquivo = open("cadastro.txt", "a+")  

    arquivo.write("Nome,Sobenome,Idade,Cidade,Estado\n")

    for i in range ( len(nomes)):
        arquivo.write(f"{nomes[i]},{sobrenomes[i]},{idades[i]},{cidades[i]},{estados[i]}\n") 
         
    arquivo.close()


if __name__ == "__main__":
    main()

Arquivo escrita

# Escrita de Arquivos

def main():

    # a+ - append - Continua escrevendo dentro do arquivo de onde parou
    # w+ - write - Limpa o arquivo antes de começar a escrever

    # 1. Abrir ou Criar o Arquivo
    arquivo = open("senai.txt", "a+")


    # 2. Manipular o arquivo (ler ou escrever)

    # 2.2 Escrita
    arquivo.write("Olá como está?\n")


    # 3. Fechar ou encerrar o Arquivo
    arquivo.close()



if __name__ == "__main__":
    main()

Arquivo leitura

# Leitura de Arquivos - txt

def main():

    # r - read - Somente leitura do arquivo
    # 1.
    # nomeArquivo = "senai.txt"
    # nomeArquivo = "E:/senai-maua/PythonMaterial/Python 315/Arquivos/senai.txt"
    nomeArquivo = "E:\\senai-maua\\PythonMaterial\\Python 315\\Arquivos\\senai.txt"
    arquivo = open(nomeArquivo, "r")

    # 2.1 
    # if arquivo.mode == 'r':
    #     conteudo = arquivo.read()
    #     print(conteudo)

    # 2.2
    if arquivo.mode == 'r':
        # readlines - ler as linhas individualmente criando 
        # uma lista com as linha
        linhas = arquivo.readlines()
        
        #2.2.1
        #print(linhas)
        
        #2.2.2
        # for lin in linhas:
        #     print(lin)

    # 3.
    arquivo.close()

if __name__ == "__main__":
    main()

Os

# OS - Operating System ou Sistema Operacional

import os

from datetime import date

def main():

    diretorio = "C:\\Temp\\"
    # diretorio = "C:/Temp"

    # Criar diretório
    # novo_diretorio = "C:/Temp/SENAI164"
    # os.makedirs(novo_diretorio)

    # Listar Diretório
    # arquivos = os.listdir(diretorio)  
    # for arquivo in arquivos:
    #     print(arquivo)

    dataHoje = str( date.today() )
    print(dataHoje)

    novo_diretorio = diretorio + dataHoje
    os.makedirs(novo_diretorio)


if __name__ == "__main__":
    main()

Automacao1

# Biblioteca do Sistema Operacional ( pastas / arquivos / caminhos)
import os

# Utilizar uma biblioteca PyPDF2 para trabalhar com PDF´s
# Instalar biblioteca: 
#   pip install pypdf2
import PyPDF2

def main():

    # Juntar 2 ou mais arquivos
    merger = PyPDF2.PdfMerger()


    lista_arquivos = os.listdir("Arquivos")
    lista_arquivos.sort()

    print(lista_arquivos)

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(f"Arquivos/{arquivo}")

    merger.write("Arquivos/PDF_Final.pdf")

if __name__ == "__main__":
    main()

Basico

Calculadora

# Funções de Operações
def somar(num1, num2):
    res = num1 + num2
    return res

def subtrair(num1, num2):
    res = num1 - num2
    return res

def multiplicar(num1, num2):
    res = num1 * num2
    return res

def dividir(num1, num2):
    res = num1 / num2
    return res

# Função Principal
def main():
    print("-------- Calculadora SENAI ---------")

    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite um outro numero: "))

    operacao = input("Digite a operação a ser calculada: ")

    if operacao == '+':
        resultado = somar(num1, num2)
        print("O resultado da operação é ", resultado)
    elif operacao == '-':
        resultado = subtrair(num1, num2)
        print("O resultado da operação é ", resultado)
    elif operacao == '*':
        resultado = multiplicar(num1, num2)
        print("O resultado da operação é ", resultado)
    elif operacao == '/':
        resultado = dividir(num1, num2) # idade = dividir(2, 9)
        print("O resultado da operação é ", resultado)
    else:
        print("Operação Invalida!!!!")   


# Ponto de Entrada para a função MAIN()
if __name__ == "__main__":
    main()

Desafio01

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

Desafio02

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

Desafio03

# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escolar
#   1. O aluno deverá digitar sua nota através do teclado
#   2. Verificar qual situação o aluno se encontra conforme notas abaixo:
#       2.1 nota > 70 - aprovado
#       2.2 nota < 40 - reprovado
#       2.3 nota entre 40 e 70 - exame/recuperação
#   3. Mostrar na tela para o aluno a situação final baseado na 
# nota digitada.

print("----- SISTEMA DE NOTAS ------")
 
nota = int(input("Digite sua nota para avaliar: "))

if nota > 70:
    print("APROVADO")
elif nota >= 40 and nota <= 70:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

Desafio04

# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [x] 1. O aluno deverá digitar 3 notas através do teclado
#   [x] 2. Seu programa deverá calcular a média das notas    
#   [x] 3. A partir da média, verificar qual situação o aluno se 
# encontra conforme media abaixo:
#       3.1 media > 70 - aprovado
#       3.2 media < 40 - reprovado
#       3.3 media entre 40 e 70 - exame/recuperação
#   [x] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [x] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro 
# de digitação
#   [x] 6. Mostrar na tela para o aluno a situação final baseado na 
# media digitada.

print("----- SISTEMA DE NOTAS ------")
 
nota1 = int(input("Digite sua nota1 para avaliar: "))
nota2 = int(input("Digite sua nota2 para avaliar: "))
nota3 = int(input("Digite sua nota3 para avaliar: "))

media = (nota1 + nota2 + nota3) / 3

if media < 0 or media > 100:
    print("Erro de digitação")
else:
    if media > 70:
        print("APROVADO")
    elif media >= 40 and media <= 70:
        print("RECUPERAÇÃO")
    else:
        print("REPROVADO")

print("FIM")

Desafio05

# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   1. O aluno deverá digitar 3 notas através do teclado
#   2. Seu programa deverá calcular a média das notas    
#   3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   4. Não será permitido médias acima de 100 e abaixo de zero
#   5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de 
# digitação
#   6. Mostrar na tela para o aluno a situação final baseado na nota 
# digitada.
#   7. Acrescente no desafio anterior a frequencia de no minimo 75% 
# para ser aprovado
#   8. O aluno pode ser aprovado se ele recebeu uma dispensa da 
# disciplina

print("----- SISTEMA DE NOTAS SENAI -----")

dispensa = input("Você possui dispensa da disicplina (S/N)?: ")

if dispensa == "S" or dispensa == "s":
    print("Você esta aprovado por dispensa")
else:
    frequencia = int(input("Digite sua frequencia: "))

    if frequencia < 75:
        print("Você reprovou por frequencia")
    else:
        nota1 = int(input("Digite sua nota1 para avaliar: "))
        nota2 = int(input("Digite sua nota2 para avaliar: "))
        nota3 = int(input("Digite sua nota3 para avaliar: "))

        media = (nota1 + nota2 + nota3) / 3

        if media < 0 or media > 100:
            print("Erro de digitação")
        else:
            if media > 70:
                print("APROVADO")
            elif media >= 40 and media <= 70:
                print("RECUPERAÇÃO")
            else:
                print("REPROVADO")

Desafio06

# ----------> Desafio 6
# Fazer um programa para o usuario digitar 2 numeros, sendo o 
# primeiro menor que o segundo e mostrar os numeros pares 
# entre esses 2 numeros
# Dica: utilizar o operador de resto - % - para descobrir
# se o numero é par

num1 = int(input("Digite o primeiro numero do intervalo: "))
num2 = int(input("Digite o segundo numero do intervalo: "))

if num1 > num2:
    # temp = num1
    # num1 = num2
    # num2 = temp
    num1 , num2 = num2, num1 


while num1 <= num2:
    if (num1 % 2) == 0:
        print(num1)

    num1 = num1 + 1

desafio06a

# ----------> Desafio 6
# Fazer um programa para o usuario digitar 2 numeros, sendo o 
# primeiro menor que o segundo e mostrar os numeros pares 
# entre esses 2 numeros
# Dica: utilizar o operador de resto - % - para descobrir
# se o numero é par

num1 = int(input("Digite o primeiro numero do intervalo: "))
num2 = int(input("Digite o segundo numero do intervalo: "))

if num1 > num2:
    num1 , num2 = num2, num1 

if (num1 % 2) == 1:
    num1 += 1

while num1 <= num2:
    print(num1)
    num1 += 2

Desafio 07

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

Desafio 08

# As maçãs custam R$0.30	 cada	 se	 forem	 compradas	menos
# do	 que	 uma dúzia,	 e	 R$	 0.25	 se	 forem	 compradas	 
# pelo menos	 doze.	 Escreva	 um	 programa	 que	 leia	 
# o	 número de	 maçãs	 compradas,	 calcule  e escreva	 o	valor	
# total	da	compra. 
# - Utilize constantes como valor unitário da maçã

# CONSTANTES
VALOR_MACA_MAIOR_12 = 0.25
VALOR_MACA_MENOR_12 = 0.30

print("------------- MAÇÃS -------------")

qtde_macas = int(input("Quantas maçãs você deseja comprar? "))

if qtde_macas >= 12:
    print("O valor da sua compra é ", (qtde_macas * VALOR_MACA_MAIOR_12))
else:
    print("O valor da sua compra é ", (qtde_macas * VALOR_MACA_MENOR_12))

Desafio 09

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


Estrutura decisao

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode dirigir")
    print("Voce DEVE votar")
    print("Voce eh maior de idade")
else:
    print("Você NÃO pode dirigir")
    print("Voce deve ter um responsavel legal")
    if idade >= 16:
        print("Voce PODE votar")
    else:
        print("Voce NÃO PODE votar, menor que 16 anos")

print("FIM")

Estrutura decisao 02

# IF / ELIF / ELSE

idade = int(input("Digite sua idade: "))

# if idade >= 0 and < 12: ERRADA!!!!

if idade >= 0 and idade < 12:
    print("Ola, voce eh uma crinça")
elif idade >= 13 and idade <= 18:
    print("Voce eh um adoslecente!!!")
elif idade >= 19 and idade <= 30:
    print("Voce eh um jovem adulto")
elif idade >= 31 and idade <= 60:
    print("Voce ja eh uma pessoa responsavel")
else:
    print("Voce entrou na melhor idade")

Estrutura repeticao

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

Excecao

# Tratamento de Exceção
def main():

    try:
        valor = int(input("Digite um numero: "))    
        resultado = 100 / valor    
    except Exception as e:
        print("ERRO: ENTRE EM CONTATO COM O SUPORTE E PASSE A MENSAGEM ABAIXO")
        print(f"MENSAGEM: {e}")
    else:
        print("O resultado eh: ", resultado)
    

    print("Fim do Programa")


if __name__ == "__main__":
    main()

Funcao biblioteca

# Biblioteca (Coleção) de Funções - "Para uma mesma finalidade"
# 
# def nomeFuncao("Argumentos da função - Dados para a função"):
    # O que a função irá fazer - Tarefa
#   return ("Resposta da Função")

VALOR_PI = 3.1415

# Funções de Operações
def somar(num1, num2):
    res = num1 + num2
    return res

def subtrair(num1, num2):
    res = num1 - num2
    return res

def multiplicar(num1, num2):
    res = num1 * num2
    return res

def dividir(num1, num2):
    res = num1 / num2
    return res

def pot(base, exp):
    res = base ** exp
    return res

