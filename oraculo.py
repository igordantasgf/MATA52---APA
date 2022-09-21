for i in range(int(input())):

    # tratamento da entrada

    entrada = input()
    k = entrada.count("!") 
    n = int(entrada.replace(k*"!",''))

    # obtendo o numero

    i=0
    fim = 1
    while(1):
        if n-(k*i)>=1:
            fim *= n-(k*i)
            i+=1
        else:
            break
    print(fim)
