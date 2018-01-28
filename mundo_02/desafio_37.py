print('converta o número digitado para binário, octal e hexadecimal')
valor = int(input('Digite o valor desejado:'))

b = bin(valor)
o = oct(valor)
h = hex(valor)

print('Selecione qual será a base de conversão, \n1 = binário \n2 = Octal \n3 = Hexadecimal')
user = int(input('qual a base de conversão?'))

if user == 1:
    print ('Valor em binário {}'.format(b))
elif user == 2:
    print ('Valor em Octal {}'.format(o))
elif user == 3:
    print ('Valor em Hexadecimal {}'.format (h))
else:
    print ('Digite o valor correto 1, 2 ou 3')