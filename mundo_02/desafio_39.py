from time import sleep
print('Quer saber se está na fase de alistamento?')
sleep(10)
idade = int(input('informe a sua idade:'))
falta = idade - 18

if idade == 18:
    print ('Siga para o serviço militar mais Próximo!')
elif idade < 18:
    print ('Ainda não pode se alistar, aguarde {}'.format(falta))
else:
    print ('Passou da idade de alistamento,você está atrasado em {} anos'.format(falta))