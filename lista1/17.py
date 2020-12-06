marc_inicial = int(input('Digite a marcação inicial: '))
marc_final = int(input('Digite a marcação final: '))
qtd_comb = int(input('Digite a qtd de combustivel gasto: '))
valor = float(input('Digite o valor recebido no dia: '))
comb = 1.90

media = (marc_final - marc_inicial) / qtd_comb
lucro = valor - (qtd_comb * comb)

print(f'Média de consumo {round(media,2)}')
print(f'Lucro: {lucro}')

