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