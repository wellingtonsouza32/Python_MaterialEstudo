sal = int(input('digite o seu salário:'))
if sal < 1250:
    aumento1 = (sal*0.15)+ sal
    print ('Você obteve um aumento de 15%, seu salário era {} e aumentou para {}'.format(sal,aumento1))

elif sal >= 1250:
    aumento2 = (sal*0.10)+ sal
    print ('Você obteve um aumento de 10%, seu salário era {} e aumentou para {}'.format(sal,aumento2))
