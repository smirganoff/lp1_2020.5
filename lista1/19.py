h1 = int(input('Digite a idade do homem: '))
h2 = int(input('Digite a idade do homem: '))
m1 = int(input('Digite a idade da mulher: '))
m2 = int(input('Digite a idade da mulher: '))

idadeh_velho = 0
idadeh_nova = 0
idadem_velho = 0
idadem_nova = 0

if h1 > h2:
    idadeh_velho = h1
    idadeh_nova = h2
else:
    idadeh_velho = h2
    idadeh_nova = h1
if m1 > m2:
    idadem_velho = m1
    idadem_nova = m2
else:
    idadem_nova = m1
    idadem_velho = m2

soma = (idadeh_velho + idadem_nova)
prod = (idadeh_nova * idadem_velho)

print(f'A soma das idades é: {soma}')
print(f'O produto das idades é: {prod}')