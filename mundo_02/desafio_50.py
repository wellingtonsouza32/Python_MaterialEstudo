soma = 0
for cont in range (0,6):
    cont += 1
    if cont == 1:
        s = 'primeiro'
    elif cont == 2:
        s = 'segundo'
    elif cont == 3:
        s = 'terceiro'
    elif cont == 4:
        s = 'quarto'
    elif cont == 5:
        s = 'quinto'
    elif cont == 6:
        s = 'sexto'
    a = int(input('digite {} valor'.format(s)))

    if a % 2 == 0:
        soma += a
    else:
        print (soma)
