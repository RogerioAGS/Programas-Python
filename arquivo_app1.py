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