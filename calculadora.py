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