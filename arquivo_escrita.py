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
