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