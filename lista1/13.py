a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
if (a < (b + c) and a > abs(b - c)) and (b < (a + c) and b > abs(a - c)) and (c < (a + b) and c > abs(a - b)):
    if a != b and b != c and a != c:
        print('O triângulo é escaleno')
    if (a == b and b != c) or (b == c and b!= a) or (a == c and a != b):
        print('O triângulo é isósceles.')
    if a == b == c:
        print('O triângulo é equilátero.')
else:
    print('Não é triângulo')