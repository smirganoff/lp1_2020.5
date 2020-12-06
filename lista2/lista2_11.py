def InvertTexto (palavra):
    invertido = palavra[::-1]
    return invertido

Texto = str(input('Digite uma palavra: '))
TextoReverso = InvertTexto(Texto)
if Texto == TextoReverso:
    print('É palíndromo.')
else:
    print('Não é palíndromo')