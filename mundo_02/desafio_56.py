sidade=0
maioridade=0
nvelho=0
nmulher=0
for a in range(0,4):
    print ('-------------Pessoa {}-------------'.format(a))
    nome = str(input('nome:')).strip()
    idade = int(input('idade:'))
    sexo = str(input('sexo: [M/F]')).strip()
    sidade += idade
    if a == 1 and sexo in 'Mm':
        maioridade = idade
        nvelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nvelho = nome
    if sexo in 'Ff' and idade <= 20:
        nmulher += 1
midade = sidade / 4
print ('a media de idade do grupo é de {} anos'.format(midade))
print('o homem mais velho tem {} anos e se chama {}.'.format(maioridade,nvelho))
print ('O número de mulher com menos de 20 anos é {}'.format(nmulher))
