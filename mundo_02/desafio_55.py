soma = 0
for a in range (0,5):
    peso = int(input("digite o peso de 5 pessoas"))
    if a == 0:
        peso1 = peso
    elif a == 1:
        peso2 = peso
    elif a == 2:
        peso3 = peso
    elif a == 3:
        peso4 = peso
    elif a == 4:
        peso5 = peso
print('Os pesos digitados em ordem foram {},{},{},{},{}'.format(peso1,peso2,peso3,peso4,peso5))
if peso1 > peso2 and peso3 and peso4 and peso5:
    print ('primeiro valor digitado {} maior de todos'.format(peso1))