cont = 0
n = int(input('Digite o número da tabuada desejada:'))
for cont in range (0,10):
    cont += 1
    if cont <= 10:
       t = n * cont
    print ('{}X{}={}'.format(cont,n,t))

