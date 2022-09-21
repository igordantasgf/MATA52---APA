# N = número de palavras
# L = linhas por página
# C = caracteres por linha
from sys import stdin

for line in stdin:
    entrada = []
    

    entrada = list(map(int,line.split()))
    n = entrada[0]
    l = entrada[1]
    c = entrada[2]
    
    texto = [''] * 100000

    livro=input().split()
    k=0
    for i in range(len(livro)):
        if len(livro[i]) > c-len(texto[k]):
            k+=1
            texto[k]=texto[k]+livro[i]+' '
        else:
            texto[k]=texto[k]+livro[i]+' '
    
    #print("linha = {}".format(k))
    k=k+1

    if (k%l!=0):
        print(int(k/l)+1)
    else:
        print(int(k/l))
