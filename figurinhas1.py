# The largest proper divisor of a number N can never be greater than N/2. 
# If a number is greater than N/2, then it can never divide N. Thus, we only loop numbers in range [1, N/2].
def procurar_mdc(ant, post):
    if(ant%post==int(0)):
        return print(post)

    val = ant
    ant = post
    post = val%post

    if(ant%post==int(0)):
        return print(post)
    else:
        procurar_mdc(ant, post)    

repeticoes = input()
repeticoes = int(repeticoes)

for i in range(repeticoes):
    player1, player2 = input().split()
    player1 = int(player1)
    player2 = int(player2)
    if(player1 <= player2):
        maior = player2
        menor = player1
    else:
        maior = player1
        menor = player2
    procurar_mdc(maior, menor)  
