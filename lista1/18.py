nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota_opt = float(input('Digite a nota optativa(caso não tenha feito, digite -1): '))

if nota_opt == -1:
    media = (nota1 + nota2)/2
elif nota1 < nota2:
    media = (nota2 + nota_opt)/2
else:
    media = (nota1 + nota_opt)/2
if media >= 6:
    print(f'Aprovado com {media}.')
elif media >= 3:
    print(f'Aluno em exame com {media}.')
else:
    print(f'Reprovado com {media}.')







