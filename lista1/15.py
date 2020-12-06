pot = int(input('Qual a potência da lâmpada em watts? '))
larg = int(input('Qual a largura do cômodo em metros?' ))
comp = int(input('Qual o comprimento do cômodo em metros?' ))

area_com = larg * comp
pot_total = area_com * 18
num_lamp = pot_total/pot

print(f'O número de lâmpadas para iluminar o cômodo é: {round(num_lamp)}')