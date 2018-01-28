print('Olá, este programa informa a condição de existência de um triângulo')

from time import sleep
sleep(2)

a = int(input('entre com o primeiro valor:'))
b = int (input('entre com o segundo valor:'))
c = int (input('entre com o terceiro valor'))

if a < (b + c) and b < (a + c) and c < (a + b):
    print ('É possível fazer um triângulo')
else:
    print('não é possível fazer um triângulo')

