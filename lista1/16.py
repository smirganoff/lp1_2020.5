comp = float(input('Digite o valor do comprimemto: '))
larg = float(input('Digite o valor da largura: '))
alt = float(input('Digite o valor da altura: '))

area = (comp * alt * 2) + (larg * alt * 2)
qtd_caixas = area/1.5

print(f'A quantidade de caixas utilizada será: {round(qtd_caixas)}.')