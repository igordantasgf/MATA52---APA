def bubble_sort(lista):
    trocado = 1
    val = len(lista)-1
    while(trocado==1):
        trocado = 0
        for i in range(0,val):
            if lista[i] < lista[i+1]:
                lista[i],lista[i+1] = lista[i+1], lista[i]
                trocado = 1
        val=val-1

loops = input()
loops = int(loops)

def analise(lista1, lista2):
    iguais=0
    for k in range(len(lista1)):
        if lista1[k]==lista2[k]:
            iguais+=1
    print(iguais)


for i in range(0,loops):
    vagoes = input()
    ordem = []
    ordem = [int(j) for j in input().split()]
    outra = [int(j) for j in ordem]
    bubble_sort(ordem)
    analise(ordem, outra)
