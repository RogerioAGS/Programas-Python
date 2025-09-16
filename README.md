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

Funcao principal

# 1ª
# Modo de uso: nomeBilioteca.nomeFuncao - ex: funcao_biblioteca.somar()
# import funcao_biblioteca

# 2ª
# Modo de uso: apelidoBiblioteca.nomeFuncao() - ex: fb.somar()
# import funcao_bibliote as fb

# 3ª
# Trazendo as funções individualmente
# Modo de uso: nomeFuncao() - ex: somar()
#from funcao_biblioteca import somar, subtrair, dividir, multiplicar 

# 4ª
# Trazer todas as funções da biblioteca 
# Modo de uso: nomeFuncao() - ex: somar()
from funcao_biblioteca import *

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

Funcoes 01

ef func1():
    print("Sou a função 1")

def func2():
    print("Sou a função 2")

def func3():
    print("Sou a função 3")


# Função Principal
def main():
    func1()
    func3()
    func1()
    func2()

    print("Sou a função principal")

if __name__ == "__main__":
    main()
    
Ola mundo

# O hashatag é utilizado para colocar um comentário na frente
# assim o que estiver na frente não será considerado pelo Python

# Instrução print() - Saída na tela
# A instrução print mostra uma mensagem/texto na tela
# A mensagem deve estar entre aspas (dupla ou simples)
print("Ola Mundo!!!, Bem vindo ao SENAI Mauá")
print('Bom dia, Turma Python 315') 


# Instrução input() - Entrada de dados pelo teclado no formato de texto
# A instrução input recebe um dado digitado e guarda em uma variável
nome = input("Digite seu nome: ")  # nome é uma variavel para guardar o que será digitado
print("Ola", nome, "seja bem vindo")
print(f"Ola {nome} seja bem vindo")

Operadores logicos

n1 = True
n2 = False

# Operador AND
res1 = n1 and n2
print("AND: ", res1)

# Operador OR
res2 = n1 or n2
print("OR: ", res1)

# Operador NOT
res3 = not n1
print("NOT: ", res3)

Ooperadores matematicos

num1 = 2
num2 = 3

# Adição
soma = num1 + num2
print("Soma: ", soma)


# Subtração
sub = num1 - num2
print("Subtração: ", sub)

# Multiplicação
mult = num1 * num2
print("Multiplicação: " , mult)

# Divisão
div = num1 / num2
print("Divisão: ", div)

# Resto
resto = num2 % num1
print("Resto: ", resto )

# Exponte
exp = num1 ** num2
print("Exponenciação: ", exp)

# Expressões:combinação dos operadores
# 1º Parênteses ()
# 2º Multiplicação/Divisão
# 3º Soma/Subtração
expressao1 = 2 * (2 * 3) + 1
print("Expressão: ", expressao1)

Operadores relacionais

# Operadores Relacionais
# O resultado da operação entre um operador relacional será verdadeiro
# True ou falso - False

n1 = 3
n2 = 2

# Igualdade ==
res1 = (n1 == n2)
print(res1)

# Diferente !=
res2 = (n1 != n2)
print(res2)

# Menor <
res3 = (n1 < n2)
print(res3)

# Menor ou igual <=
res4 = (n1 <= n2)
print(res4)

# Maior >
res5 = (n1 > n2)
print(res5)

# Maior ou igual >=
res6 = (n1 >= n2)
print(res6)

Teste

nome = "Teste"

nome = nome.lower()

print (nome)

Variaveis 01

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

Variaveis 02 p1

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

Variaveis 02 p2

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

Classes

class Carro:
    # Caracteristicas Iniciais do Objeto
    # Método Construtor: executado automaticamente quando o objeto é criado
    def __init__(self, marca, modelo):
        self.ano = 0
        self.marca = marca
        self.modelo = modelo


    # Funcionalidade (funções -> métodos)
    def imprimirDados(self):
        print(f"O carro é da marca {self.marca}  e o modelo dele é {self.modelo}")


def main():

    # Criar um Objeto
    carro1 = Carro("Toyota", "Etios")
    carro2 = Carro("Fiat", "Uno")
    
    carro1.imprimirDados()
    carro2.imprimirDados()

if __name__ == "__main__":
    main()

Flet

# Biblioteca Flet (Flutter) - https://flet.dev
# pip install flet
# flet run main.py

import flet as ft

def main(page: ft.Page):

    def subtrair(e):
        numero = int(txt_numero.value)
        numero -= 1
        txt_numero.value = str(numero)

        if numero < 10:
            txt_numero.bgcolor = ft.colors.BLUE        

        page.update()

    def somar(e):
        numero = int(txt_numero.value)
        numero += 1
        txt_numero.value = str(numero)

        if numero >= 10:
            txt_numero.bgcolor = ft.colors.ORANGE_900

        page.update()



    page.title = "SENAI - Flet Básico"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    btn_menos = ft.IconButton(ft.icons.REMOVE, on_click=subtrair)
    btn_mais = ft.IconButton(ft.icons.ADD, on_click=somar)

    txt_numero = ft.TextField(
        value="0",
        bgcolor=ft.colors.BLUE,
        width=100,
        border_radius=20,
        text_align=ft.TextAlign.CENTER,
        read_only=True,
        color=ft.colors.BLACK87
    )

    page.add(
        ft.Row(
            [
                btn_menos,
                txt_numero,
                btn_mais
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )               
    )
ft.app(target=main)

Pygame

bat

import pygame
import random

class Bat(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bat-x4.gif")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(900, 50, 100, 100)

        self.rect.x = 840 + random.randint(1,400)
        self.rect.y = random.randint(2, 400)

        self.speed = 1 + random.random() * 2

    def update(self, *args):

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

Ghost

import pygame

class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        # Carregar a imagem para uso
        self.image = pygame.image.load("data/ghost-x4.gif")
        # Redimensionar a imagem para completar nosso retângulo em 100%
        self.image = pygame.transform.scale(self.image, [100, 100])
        # Posicionando e dimensionando o retangulo na tela
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speedX = 0
        self.accelerationX = 0.1

        self.speedY = 0
        self.accelerationY = 0.1

    def update(self, *args):

        # Evento Movimentação
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.speedY += self.accelerationY
        elif keys[pygame.K_UP]:
            self.speedY -= self.accelerationY
        if keys[pygame.K_RIGHT]:
            self.speedX += self.accelerationX
        elif keys[pygame.K_LEFT]:
            self.speedX -= self.accelerationX
        else:
            self.speedY *= 0.95
            self.speedX *= 0.95

        self.rect.y += self.speedY
        self.rect.x += self.speedX

        # Limite de Tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speedY = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedX = 0
        elif self.rect.right > 840:
            self.rect.right = 840
            self.speedX = 0

Main

# 0. Criar uma instalação Desktop ------------------------------------

# PASSO 1: Digitar o seguinte código comentado abaixo:

# Importa os módulos os (para interagir com o sistema operacional) e 
# sys (para acessar variáveis e funções do interpretador Python).
import os, sys  

# Obtém o caminho completo do diretório onde o script está sendo executado e armazena em dirpath.
dirpath = os.getcwd()  

# Adiciona o diretório atual ao caminho de busca do Python. Isso permite que o Python encontre módulos 
# localizados no mesmo diretório que o script. No caso as subpastas com os assets
sys.path.append(dirpath)  

# Verifica se o script está sendo executado como um executável compilado 
# (por exemplo, usando PyInstaller).
if getattr(sys, "frozen", False):  
    os.chdir(sys._MEIPASS)  # Se estiver compilado, muda o diretório de trabalho atual 
                            # para o diretório onde os arquivos do aplicativo foram extraídos.


# PASSO 2: Após a inserção do código acima instalar o pyinstaller no terminal com o comando: 
#  - pip install pyinstaller    


# PASSO 3: Executar o seguinte comando no terminal (o parametro -F é para colocar em um único arquivo):
#  - pyinstaller -F main.py

# PASSO 4: Abrir o arquivo main.spec e alterar o item: datas=[("data", "data")] como mostrado abaixo
#  a = Analysis(
#     ['main.py'],
#     pathex=[],
#     binaries=[],
#     datas=[("data", "data")],
#     hiddenimports=[],
#     hookspath=[],
#     hooksconfig={},
#     runtime_hooks=[],
#     excludes=[],
#     noarchive=False,
#     optimize=0,
# )

# PASSO 5: Executar o seguinte comando no terminal:
#  - pyinstaller main.spec

# PASSO 6: Verificar o arquivo executavel na pasta dist


# Pygame:
#   - Instalar a biblioteca no terminal: pip install pygame


# 1. IMPORTS -------------------------------------------------------------------
import pygame
import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot


# 2. INICIALIZAÇÃO--------------------------------------------------------------

# 2.1 Iniciar Pygame
pygame.init()

# 2.2 Iniciar a janela com a configuração de resolução de 840x480

# 2.2.1 Constantes de largura e altura de tela
LARGURA_TELA = 840
ALTURA_TELA = 480

# 2.2.2 Criar a janela
display = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])

# 2.2.3 Preencher o fundo da janela com uma cor RGB
display.fill([66, 135, 245])
# 2.2.4 Preencher o fundo da janela com uma cor em HEX
# display.fill("#4287f5")

# 2.2.5 Mudar o título da janela
pygame.display.set_caption("Game SENAI - Python 315")

# 2.2.6 Carregar a imagem do icone e mudar o icone da janela
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)


# 3. ELEMENTOS DE TELA ---------------------------------------------------------

# 3.1 Personagens

# Criar um grupo de imagens para inserir todas as imagens e desenhar elas de uma 
# única vez 
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

# Criar um cenário (background) para o fantasma
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

# Criar um objeto da Classe Ghost e coloco no grupo objectGroup
ghost = Ghost(objectGroup)

# 3.2 Fontes ------------------------------------------------------------------
score_font = pygame.font.Font("data/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("data/Pixeltype.ttf", 200)

# 3.3 Música ------------------------------------------------------------------
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1) # -1 para ser um loop infinito

# 3.4 Som (SFX) ------------------------------------------------------------------
attack = pygame.mixer.Sound("data/magic1.wav")


# 4. VARIAVEIS GLOBAIS ---------------------------------------------------------
gameLoop = True
gameOver = False

timer = 20
pontos = 0


# 4.1 Criar um clock para ajustar os frames por segundo (fps)
clock = pygame.time.Clock()



# 5. FUNÇÃO PRINCIPAL ----------------------------------------------------------
def main():

    global gameLoop
    global gameOver
    global timer
    global pontos
   
    while gameLoop:
        # Clock de 60fps
        clock.tick(60)

        # Loop de Eventos - Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN: # Evento Tiros
                if event.key == pygame.K_SPACE:
                    if Shoot.numTiros < 5:
                        newShoot = Shoot(objectGroup, shootGroup)
                        newShoot.rect.center = ghost.rect.center
                        attack.play()

        if not gameOver:
                
            display.fill([66, 135, 245])

            # Criar varios morcegos
            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup) 

            # Colisao dos Morcegos com o Fantasma
            colisao = pygame.sprite.spritecollide(
                ghost,
                batGroup,
                False,
                pygame.sprite.collide_mask
            )

            if colisao:
                gameOver = True
                print("GAME OVER!!!")

            # Colisao do tiro com o morcego
            tiros = pygame.sprite.groupcollide(
                shootGroup,
                batGroup,
                True,
                True,
                pygame.sprite.collide_mask
            )

            if tiros:
                pontos += 1
                print("SCORE: ", pontos)
                Shoot.subtrairTiros()

            # Atualizar a posição do objetos
            objectGroup.update()

        # Desenhar na tela
        objectGroup.draw(display)

        # Inserir a pontuação na tela
        score_render = score_font.render(f"Score: {pontos}", False, "White")
        display.blit(score_render, (650,50))

        # Inserir a mensagem GAME OVER na tela
        if gameOver:
            gameOverMsg = gameOver_font.render("GAME OVER", False, "White")
            display.blit(gameOverMsg, (100,150))

        # Atualização da tela
        pygame.display.update()


if __name__ == "__main__":
    main()

README

<h1>Desenvolvimento de Jogos - Pilares</h1>

1. Janelas
    - Criar janelas para o nosso sistema/jogo

2. Reconhecer os Inputs (Interação com o Jogador)
    - Teclado,
    - Mouse,
    - etc...

3. Pintar e desenhar coisas na tela (janela)
    - Animação

4. Lógica
    - Executar lógicas para a dinâmica do jogo,
    - Física

5. Áudio - como o som trabalha ajundando o desenrolar do jogo
    - Música,
    - Efeitos
  
Shoot

import pygame

class Shoot(pygame.sprite.Sprite):
    
    numTiros = 0

    @staticmethod
    def somarTiros():
        Shoot.numTiros += 1
    
    @staticmethod
    def subtrairTiros():
        Shoot.numTiros -= 1

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [50,50])

        # self.rect = pygame.Rect(50, 50, 100, 100)
        self.rect = self.image.get_rect()
        
        self.speed = 4

        Shoot.somarTiros()

    def update(self, *args):

        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
            Shoot.subtrairTiros()

Pygame - Upgrade

bat

import pygame
import random

class Bat(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bat-x4.gif")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(900, 50, 100, 100)

        self.rect.x = 840 + random.randint(1,400)
        self.rect.y = random.randint(2, 400)

        self.speed = 1 + random.random() * 2

    def update(self, *args):

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

ghost

import pygame

class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        # Carregar a imagem para uso
        self.image = pygame.image.load("data/ghost-x4.gif")
        # Redimensionar a imagem para completar nosso retângulo em 100%
        self.image = pygame.transform.scale(self.image, [100, 100])
        # Posicionando e dimensionando o retangulo na tela
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speedX = 0
        self.accelerationX = 0.1

        self.speedY = 0
        self.accelerationY = 0.1

    def update(self, *args):

        # Evento Movimentação
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speedY += self.accelerationY
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speedY -= self.accelerationY
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speedX += self.accelerationX
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speedX -= self.accelerationX
        else:
            self.speedY *= 0.95
            self.speedX *= 0.95

        self.rect.y += self.speedY
        self.rect.x += self.speedX

        # Limite de Tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speedY = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedX = 0
        elif self.rect.right > 840:
            self.rect.right = 840
            self.speedX = 0

main

# 0. Criar uma instalação Desktop ------------------------------------

# PASSO 1: Digitar o seguinte código comentado abaixo:

# Importa os módulos os (para interagir com o sistema operacional) e 
# sys (para acessar variáveis e funções do interpretador Python).
import os, sys  

# Obtém o caminho completo do diretório onde o script está sendo executado e armazena em dirpath.
dirpath = os.getcwd()  

# Adiciona o diretório atual ao caminho de busca do Python. Isso permite que o Python encontre módulos 
# localizados no mesmo diretório que o script. No caso as subpastas com os assets
sys.path.append(dirpath)  

# Verifica se o script está sendo executado como um executável compilado 
# (por exemplo, usando PyInstaller).
if getattr(sys, "frozen", False):  
    os.chdir(sys._MEIPASS)  # Se estiver compilado, muda o diretório de trabalho atual 
                            # para o diretório onde os arquivos do aplicativo foram extraídos.


# PASSO 2: Após a inserção do código acima instalar o pyinstaller no terminal com o comando: 
#  - pip install pyinstaller    


# PASSO 3: Executar o seguinte comando no terminal (o parametro -F é para colocar em um único arquivo):
#  - pyinstaller -F main.py

# PASSO 4: Abrir o arquivo main.spec e alterar o item: datas=[("data", "data")] como mostrado abaixo
#  a = Analysis(
#     ['main.py'],
#     pathex=[],
#     binaries=[],
#     datas=[("data", "data")],
#     hiddenimports=[],
#     hookspath=[],
#     hooksconfig={},
#     runtime_hooks=[],
#     excludes=[],
#     noarchive=False,
#     optimize=0,
# )

# PASSO 5: Executar o seguinte comando no terminal:
#  - pyinstaller main.spec

# PASSO 6: Verificar o arquivo executavel na pasta dist

#########################################################################################################
# Pygame:
#   - Instalar a biblioteca no terminal: pip install pygame


# 1. IMPORTS -------------------------------------------------------------------
import pygame
import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot
from pumpkin import Pumpkin


# 2. INICIALIZAÇÃO--------------------------------------------------------------

# 2.1 Iniciar Pygame
pygame.init()

# 2.2 Iniciar a janela com a configuração de resolução de 840x480

# 2.2.1 Constantes de largura e altura de tela
LARGURA_TELA = 840
ALTURA_TELA = 480

# 2.2.2 Criar a janela
display = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])

# 2.2.3 Preencher o fundo da janela com uma cor RGB
display.fill([66, 135, 245])
# 2.2.4 Preencher o fundo da janela com uma cor em HEX
# display.fill("#4287f5")

# 2.2.5 Mudar o título da janela
pygame.display.set_caption("Game SENAI - Python 315")

# 2.2.6 Carregar a imagem do icone e mudar o icone da janela
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)


# 3. ELEMENTOS DE TELA ---------------------------------------------------------

# 3.1 Personagens

# Criar um grupo de imagens para inserir todas as imagens e desenhar elas de uma 
# única vez 
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()


# 3.2 Fontes ------------------------------------------------------------------
score_font = pygame.font.Font("data/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("data/Pixeltype.ttf", 200)

# 3.3 Música ----------------------------------------------------------
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1)  # -1 para ser um loop infinito

# 3.4 Som (SFX) ------------------------------------------------------
attack = pygame.mixer.Sound("data/magic1.wav")

# 4. VARIAVEIS GLOBAIS ---------------------------------------------------------
gameLoop = True
gameOver = False

timer = 20
pontos = 0

numSetupFase = 1
numfase = 1

vidas = 3

# 4.1 Criar um clock para ajustar os frames por segundo (fps)
clock = pygame.time.Clock()


# 5. FUNÇÃO PRINCIPAL ----------------------------------------------------------
def main():

    global gameLoop
    global gameOver
    global timer
    global pontos
    global numSetupFase
    global numfase
    global vidas
   

    while gameLoop:
        # Clock de 60fps
        clock.tick(60)


        if numSetupFase == 1:
            # Criar um cenário (background) para o fantasma
            bg = pygame.sprite.Sprite(objectGroup)
            bg.image = pygame.image.load("data/background.jpg")
            bg.image = pygame.transform.scale(bg.image, [840, 480])
            bg.rect = bg.image.get_rect()

            # Criar um objeto da Classe Ghost e coloco no grupo objectGroup
            ghost = Ghost(objectGroup)

            numSetupFase = 0
            numfase = 1

        if numSetupFase == 2:
            # Criar um cenário (background) para o fantasma
            bg = pygame.sprite.Sprite(objectGroup)
            bg.image = pygame.image.load("data/bg_fase2.jpg")
            bg.image = pygame.transform.scale(bg.image, [840, 480])
            bg.rect = bg.image.get_rect()

            # Criar um objeto da Classe Ghost e coloco no grupo objectGroup
            ghost = Ghost(objectGroup)

            numSetupFase = 0
            numfase = 2

        # Loop de Eventos - Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN: # Evento Tiros
                if event.key == pygame.K_SPACE:
                    if Shoot.numTiros < 5:
                        newShoot = Shoot(objectGroup, shootGroup)
                        newShoot.rect.center = ghost.rect.center
                        attack.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Shoot.numTiros < 5:
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = ghost.rect.center
                    attack.play()

        if not gameOver:
                
            
            timer += 1

            # Criar varios morcegos
            if timer > 30 and numfase == 1:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup) 

            # Criar varios morcegos e aboboras
            if timer > 30 and numfase == 2:
                timer = 0
                if random.random() < 0.45:
                    newBat = Bat(objectGroup, batGroup) 
                if random.random() < 0.25:
                    newPumpkin = Pumpkin(objectGroup, batGroup) 

            # Colisao dos Morcegos com o Fantasma
            colisao = pygame.sprite.spritecollide(
                ghost,
                batGroup,
                True,
                pygame.sprite.collide_mask
            )

            if colisao:
                vidas -= 1
                
            if vidas == 0:
                gameOver = True

            # Colisao do tiro com o morcego
            tiros = pygame.sprite.groupcollide(
                shootGroup,
                batGroup,
                True,
                True,
                pygame.sprite.collide_mask
            )

            if tiros:
                pontos += 1
                Shoot.subtrairTiros()

                if pontos ==  10:
                    ghost.kill()
                    numSetupFase = 2

            # Atualizar a posição do objetos
            objectGroup.update()

        # Desenhar na tela
        objectGroup.draw(display)

        # Inserir a pontuação na tela
        score_render = score_font.render(f"Score: {pontos}", False, "White")
        display.blit(score_render, (650,50))

        # Vidas
        score_render = score_font.render(f"Life: {vidas}", False, "White")
        display.blit(score_render, (50,50))

        # Inserir a mensagem GAME OVER na tela
        if gameOver:
            gameOverMsg = gameOver_font.render("GAME OVER", False, "White")
            display.blit(gameOverMsg, (100,150))

        # Atualização da tela
        pygame.display.update()

if __name__ == "__main__":
    main()

pumpkin

import pygame
import math
import random

class Pumpkin(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/pumpkin2-removebg.png")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(900, 50, 100, 100)


        self.rect.x = 840 + random.randint(1,400)
        self.rect.y = random.randint(2, 400)

        self.speed = 1 + random.random() * 2

        self.timer = 0

    def update(self, *args):

        self.timer += 0.001

        self.rect.x -= self.speed

        self.rect.y = self.rect.y + ( math.sin(self.timer) * 2)

        if self.rect.right < 0 or self.rect.top > 500:
            self.kill()


README

<h1>Desenvolvimento de Jogos - Pilares</h1>

1. Janelas
    - Criar janelas para o nosso sistema/jogo

2. Reconhecer os Inputs (Interação com o Jogador)
    - Teclado,
    - Mouse,
    - etc...

3. Pintar e desenhar coisas na tela (janela)
    - Animação

4. Lógica
    - Executar lógicas para a dinâmica do jogo,
    - Física

5. Áudio - como o som trabalha ajundando o desenrolar do jogo
    - Música,
    - Efeitos
  
shoot

import pygame

class Shoot(pygame.sprite.Sprite):
    
    numTiros = 0

    @staticmethod
    def somarTiros():
        Shoot.numTiros += 1
    
    @staticmethod
    def subtrairTiros():
        Shoot.numTiros -= 1

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [50,50])

        # self.rect = pygame.Rect(50, 50, 100, 100)
        self.rect = self.image.get_rect()
        
        self.speed = 4

        Shoot.somarTiros()

    def update(self, *args):

        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
            Shoot.subtrairTiros()

SQLite

main

import sqlite3

def main():

    # 1. Conectar com o bando de dados
    #   - Criar uma conexão e um cursor. O cursor será utilizado
    # para executar querys(CRUD)
    #   - Caso o banco de dados não exista a biblioteca sqlite
    #  irá criar 
    conn = sqlite3.connect("db_python.db")
    cursor = conn.cursor()

    # 2. Executar Querys - CRUD

    # -------------------- Criar Tabela 
    # queryTabela = '''CREATE TABLE IF NOT EXISTS "Contatos" (
    #     "id"        INTEGER,
    #     "nome"      TEXT,
    #     "sobrenome" TEXT,
    #     "email"     TEXT,
    #     PRIMARY KEY( "id" AUTOINCREMENT)    
    # );'''

    # cursor.execute(queryTabela)

    # -------------------------- Inserir Dados
    # nome = input("Digite o nome: ")
    # sobrenome = input("Digite o sobrenome: ")
    # email = input("Digite o email: ")

    # queryInsert = f'''INSERT INTO Contatos (nome, sobrenome, email)
    #     VALUES("{nome}", "{sobrenome}", "{email}")

    # ;'''

    # cursor.execute(queryInsert)

    # ------------------- Atualizar dados : EMAIL
    # email = input("Digite o novo email: ")
    # num_registro = int(input("Digite o numero do registro: "))

    # queryUpdate = f'''UPDATE Contatos SET email="{email}" 
    #     WHERE id="{num_registro}";'''
    
    # cursor.execute(queryUpdate)

    # --------------------- Apagar Registro
    # num_registro = int(input("Digite o numero do registro: "))

    # queryDelete = f'''DELETE FROM Contatos 
    #     WHERE id="{num_registro}";'''
    
    # cursor.execute(queryDelete)
    
    # ---------------------- Selecionar Registros
    querySelect = '''SELECT * FROM Contatos;'''

    resultadoSelect = cursor.execute(querySelect)

    for valor in resultadoSelect:
        print(valor)

    # 3. Efetivar as Querys dentro do BD - Commit
    #  OBS: Não é necessário para o SELECT
    conn.commit()


    # 4. Fechar a conexão com o BD (Finalizar a transação)
    conn.close()


if __name__ == "__main__":
    main()
