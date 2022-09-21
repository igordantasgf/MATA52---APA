# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 1 0 1
# 0 0 1 0 1
# 1 0 1 0 0

def analise(lista,index,res):
    #print("Lista: {}".format(res))
    if index==24:
        res[0]=1
        #print("Set do val = 1")
        return res

    # UP, RIGHT, DOWN, LEFT: DFS(Depth first search)
    #up
    if index>4 and lista[index-5]=='0':
        lista[index]='1'
        analise(lista,index-5,val)
    #right
    if (index+1)%5!=0 and lista[index+1]=='0':
        lista[index]='1'
        analise(lista,index+1,val)
    #down
    if index<20 and lista[index+5]=='0':
        lista[index]='1'
        analise(lista,index+5,val)
    #left
    if index%5!=0 and lista[index-1]=='0':
        lista[index]='1'
        analise(lista,index-1,val)
    

op = int(input()) # número de operações


for i in range(0,op):

    matriz = []
    while(len(matriz)<25):
        matriz.extend(input().split())
    #print(matriz)
    val = []

    if matriz[0]=='1':
        print("ROBBERS")
        continue

    val.append(0)
    analise(matriz,0,val)
    #print("Valor return: {}".format(analise(matriz,0,val)))

    #print("Val é {}".format(val))
    if val[0]==1:
        print("COPS")
    else:
        print("ROBBERS")
