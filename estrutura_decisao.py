

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode dirigir")
    print("Voce DEVE votar")
    print("Voce eh maior de idade")
else:
    print("Você NÃO pode dirigir")
    print("Voce deve ter um responsavel legal")
    if idade >= 16:
        print("Voce PODE votar")
    else:
        print("Voce NÃO PODE votar, menor que 16 anos")

print("FIM")