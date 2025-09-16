# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [x] 1. O aluno deverá digitar 3 notas através do teclado
#   [x] 2. Seu programa deverá calcular a média das notas    
#   [x] 3. A partir da média, verificar qual situação o aluno se 
# encontra conforme media abaixo:
#       3.1 media > 70 - aprovado
#       3.2 media < 40 - reprovado
#       3.3 media entre 40 e 70 - exame/recuperação
#   [x] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [x] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro 
# de digitação
#   [x] 6. Mostrar na tela para o aluno a situação final baseado na 
# media digitada.

print("----- SISTEMA DE NOTAS ------")
 
nota1 = int(input("Digite sua nota1 para avaliar: "))
nota2 = int(input("Digite sua nota2 para avaliar: "))
nota3 = int(input("Digite sua nota3 para avaliar: "))

media = (nota1 + nota2 + nota3) / 3

if media < 0 or media > 100:
    print("Erro de digitação")
else:
    if media > 70:
        print("APROVADO")
    elif media >= 40 and media <= 70:
        print("RECUPERAÇÃO")
    else:
        print("REPROVADO")

print("FIM")