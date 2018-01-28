n1 = int (input('Digite um número:'))
a = n1 - 1
s = n1 + 1
print('você digitou {} seu antecessor é {} seu sucessor é {}'.format(n1,a,s))

#de outra forma economiza memória quanto menos usar variável

print('Execução da segunda forma')
n1 = int (input('Digite um número:'))
print('você digitou {} seu antecessor é {} seu sucessor é {}'.format(n1,n1 - 1,n1 + 1))
