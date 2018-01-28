import random
u = int(input('digite um número de 0 a 5!')
c = random.randint(0,5)
if (u is None):
    print('está vazio ou digitou número incorreto, tente novamente!')
elif  u == c:
    print ('Parabéns você acertou!')
else:
    print ('Você errou, tente novamente')
