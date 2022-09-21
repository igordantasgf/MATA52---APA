rep = int(input())
lista_fib=[0]*40
lista_calls=[0]*40

lista_fib[1]=1
lista_fib[2]=1
lista_calls[0]=1
lista_calls[1]=1
lista_calls[2]=2
lista_calls[3]=4

for i in range(3,40):
    lista_fib[i]=lista_fib[i-1]+lista_fib[i-2]

for i in range(4,40):
    lista_calls[i]=lista_calls[i-1]+1+lista_calls[i-2]+1

for i in range(rep):
    x = int(input())
    print('fib({}) = {} calls = {}'.format(x,lista_calls[x],lista_fib[x]))
    
