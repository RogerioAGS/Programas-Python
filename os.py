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