import random
print ('vamos jogar jokenpô?')

j = int(input('escolha 1:pedra 2:tesoura 3:papel'))

lista = ['pedra','papel','tesoura']

r = random.choice(lista)

if j == r:
    print ('empate')
elif j == 3 and r == 'tesoura':
    print ('você jogou {} e computador {} e voce perdeu'.format('papel',r))
elif j == 3 and r == 'pedra':
    print ('você jogou {} e computador {} e voce ganhou'.format('papel',r))
elif j == 2 and r == 'papel':
    print ('você jogou {} e o computador {} e voce ganhou'. format('tesoura',r))
elif j == 2 and r == 'pedra':
    print ('você jogou {} e o computador {} e voce perdeu'.format('tesoura',r))
elif j == 1 and r == 'papel':
    print('você jogou {} e o computador {} e voce perdeu'.format('pedra',r))
elif j == 1 and r == 'tesoura':
    print ('você jogou {} e o computador {} e voce ganhou'.format('pedra',r))
else:
    print('tente novamente!')