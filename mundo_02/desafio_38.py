um = int(input('digite primeiro número:'))
dois = int (input('digite segundo numero'))

if um > dois:
    print('primeiro valor {} é maior que o segundo {}'.format(um,dois))
elif um < dois:
    print ('Segundo valor {} é maior que o primeiro {}'.format(dois,um))
else:
    print('Primeiro valor {} e segundo valor {} são iguais'.format(um,dois))