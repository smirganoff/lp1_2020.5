a = int(input('Digite o valor de um ângulo: '))
b = int(input('Digite o valor de um ângulo: '))
c = int(input('Digite o valor de um ângulo: '))
if a + b +c == 180:
    if a == 90 or b == 90 or c == 90:
        print('O triângulo é retângulo.')
    if a > 90 or b > 90 or c > 90:
        print('O triângulo é obtuso.')
    if a < 90 and b < 90 and c < 90:
        print('O triângulo é acutângulo.')
else:
    print('Não é um triângulo.')