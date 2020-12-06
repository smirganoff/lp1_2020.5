A = [1, 2, 3], [4, 5, 6], [7, 8, 9]
B = [10, 11, 12], [13, 14, 15], [16, 17, 18]
C = 0
def mat_mult (A, B):
    linha_A, coluna_A = len(A), len(A[0])
    linha_B, coluna_B = len(B), len(B[0])
    C = []
    for linha in range(linha_A):
        C.append([])
        for coluna in range(coluna_B):
            C[linha].append(0)
            for k in range(coluna_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C
print(f'{mat_mult(A, B)}')