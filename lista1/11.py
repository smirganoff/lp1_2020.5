a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

if (a < (b + c) and a > abs(b - c)) and (b < (a + c) and b > abs(a - c)) and (c < (a + b) and c > abs(a - b)):
    print('É um triângulo')
else:
    print('Não é um triângulo')