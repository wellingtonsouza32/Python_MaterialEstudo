a = float(input('Digite o valor do produto:'))

mp = int(input('Selecione a forma de pagamento "1" para cartão e "2" para dinheiro:'))
if mp == 1:
    print ('Método de pagamento Cartão')
elif mp == 2:
    print ('Método de pagamento Dinheiro')
else:
    print ('Método de pagamento desconhecido')

fp = int (input('Para forma de pagamento digite 1 para "à vista" e 2 para "parcelamento"'))

if fp == 1:
     print ('forma selecionada À Vista')
elif fp == 2:
    qnt = int(input('Digite quantidade de parcelas:'))
else:
    print('forma de pagamento desconhecida')

if mp == 1 and fp == 1:
    pcv = a - (a * 0.05)
    print ('Valor a ser pago {}'.format(pcv))
elif mp == 2 and fp == 1:
    pdv = (a * 0.10) - a
    print('Valor a ser pago é {}'.format(pdv))
elif mp == 1 and fp == 2 and qnt == 2:
    ppc = a / 2
    print('pagamento será realizado em duas vezes, valor da parcela {}'.format(ppc))
elif mp == 1 and fp == 2 and qnt > 2:
    ppcm = ((a * 0.2) + a) / qnt
    print('pagamento será parcelado em {} vezes, valor da parcela{}'.format(qnt,ppcm))
else:
    print('forma de pagamento inválido!')
