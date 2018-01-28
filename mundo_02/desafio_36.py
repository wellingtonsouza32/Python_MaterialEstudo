sal = float (input('Qual o valor do salário:'))
anos = float (input('Quantos anos pagará o imóvel:'))
casa = float (input('Valor da casa:'))

p = casa / (anos * 12)


if p > sal :
    print('Empréstimo não aprovado')
else:
    print('Seu salário é {} e o valor da parcela é {:.2f} Empréstimo aprovado!'.format(sal,p))