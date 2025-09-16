# IF / ELIF / ELSE

idade = int(input("Digite sua idade: "))

# if idade >= 0 and < 12: ERRADA!!!!

if idade >= 0 and idade < 12:
    print("Ola, voce eh uma crinça")
elif idade >= 13 and idade <= 18:
    print("Voce eh um adoslecente!!!")
elif idade >= 19 and idade <= 30:
    print("Voce eh um jovem adulto")
elif idade >= 31 and idade <= 60:
    print("Voce ja eh uma pessoa responsavel")
else:
    print("Voce entrou na melhor idade")