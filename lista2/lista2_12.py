word1 = str(input('Digite uma palavra:'))
word2 = str(input('Digite uma palavra:'))

Tamanho1 = (len(word1))
Tamanho2 = (len(word2))

if len(word1) != len(word2):
    print('não é um anagrama')
else:
    for i in range(Tamanho1):
        for j in range(Tamanho2):
            if (word1[i]) == (word2[j]):
                word2 = word2[0:j-1]+ '0'+word2[j+1:Tamanho2]
    Verifica = 1
    for k in range(Tamanho2):
        if word2[k] != "0":
            Verifica = 0
    if Verifica == 1:
        print('é um anagrama')
    else:
        print('não é um anagrama')


