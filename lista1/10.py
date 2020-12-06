a = int(input('Digite um número: '))
cont = 0

for i in range (2,a):
  if a % i == 0:
    cont = cont + 1
if cont == 0:
    print('é primo')
else:
    print('não é primo')
