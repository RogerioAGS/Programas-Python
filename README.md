Agenda_SQLite
    
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
    main()# Programas-Python
