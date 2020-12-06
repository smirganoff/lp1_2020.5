matriz_A = [1, 2, 3 ],[4, 5, 6 ], [7, 8, 9 ]
matriz_B = [9, 8, 7 ],[6, 5, 4 ], [3, 2, 1 ]
matriz_C = [0, 0, 0], [0, 0, 0], [0, 0, 0]
subtracao = 0

def soma(matriz_A, matriz_B):
   qtd_colunas = len(matriz_A[0])
   qtd_linhas = len(matriz_A)
   for i in range(qtd_colunas):
        for j in range(qtd_linhas):
            matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]
   return matriz_C


def subtracao(matriz_A, matriz_B):
    qtd_colunas = len(matriz_A[0])
    qtd_linhas = len(matriz_A)
    for i in range(qtd_colunas):
        for j in range(qtd_linhas):
          matriz_C[i][j] = matriz_A[i][j] - matriz_B[i][j]
    return matriz_C

def multiplicacao(matriz_A, matriz_B):
    qtd_colunas = len(matriz_A[0])
    qtd_linhas = len(matriz_A)
    for i in range(qtd_colunas):
        for j in range(qtd_linhas):
            matriz_C[i][j] = matriz_A[i][j] * matriz_B[i][j]
    return matriz_C

matriz_soma = soma(matriz_A, matriz_B)
print(matriz_soma)

matriz_subtracao = subtracao(matriz_A, matriz_B)
print(matriz_subtracao)

matriz_mult = multiplicacao(matriz_A, matriz_B)
print(matriz_mult)

