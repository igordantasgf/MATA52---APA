from math import sqrt

def search(lista, visitados, node, idas):
    for i in lista:
        #print("Analisando : ",i)
        if i[0]==node:
            if visitados[i[1]]==False:
                #print("idas++: indo de {} para {}".format(i[0],i[1]))
                idas+=1
                idas = dfs(lista, visitados, i[1], idas)
                #print("Novo idas = ",idas)
        elif i[1]==node:
            if visitados[i[0]]==False:
                #print("idas++: indo de {} para {}".format(i[1],i[0]))
                idas+=1
                idas = dfs(lista, visitados, i[0], idas)
                #print("Novo idas = ",idas)


    return idas

def dfs(lista, visitados, node, idas): 
    visitados[node]=True
    for l in lista:
        if l[0]==node:
            #print("l[1]=",l[1])
            if visitados[l[1]]==False:
                idas+=1
                #print("idas++: indo de {} para {}".format(l[0],l[1]))
                idas = dfs(lista, visitados, l[1], idas)
        elif l[1]==node:
            if visitados[l[0]]==False:
                idas+=1
                #print("idas++: indo de {} para {}".format(l[1],l[0]))
                idas = dfs(lista, visitados, l[0], idas)
    idas+=1
    #print("Voltando para: ",node)
    return idas

tamanho = int(input())

for x in range(tamanho):

    node = int(input())
    v,a=[int(k) for k in input().split()]
    lista = []
    n = int(sqrt(v))
    
    

    for j in range(a):
        elementos = 0
        lista.append(sorted([int(k) for k in input().split()]))
        #lista.append([50,50]*20)
    #print("Tamanho de visitados: ", len(lista))
    visitados = [False]*(v+1)
    visitados[node]=True
    #print(lista)
    idas=0
    print(search(lista, visitados,node,idas))
