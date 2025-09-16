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