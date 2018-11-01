import time
data = int(time.strftime('%Y'))
soma=0
for a in range (0,7):
    nasc = int(input("digite uma data de nascimento"))
    soma += 1
    if soma <= 7:
        r = data - nasc
        if r >= 18:
            print('a idade é {} considerado maior de idade'.format(r))
        else:
            print ("Ainda é menor de idade")
    else:
        print ('fim')