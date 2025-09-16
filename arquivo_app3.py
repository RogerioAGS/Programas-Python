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