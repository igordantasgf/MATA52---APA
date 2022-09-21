#from sys import stdin

#for line in stdin:
while True:
    try:
        n = int(input())
        diaria = int(input())
        lista_diaria=[]
        for j in range(n):
            lista_diaria.append(int(input()))
        resultado=[]

        for j in range(0,n):
            resultado.append(-diaria+lista_diaria[j])

        soma_final = resultado[0]
        soma = resultado[0]

        for i in range(1,n):
            soma = max(resultado[i], soma + resultado[i])
            soma_final = max(soma_final,soma)

        if soma_final<=0:
            print(0)
        else:
            print(soma_final)
        #do something

    except EOFError:
        break
