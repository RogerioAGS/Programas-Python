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
