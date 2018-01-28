a= int(input("digite o número:"))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print('unidade:{}'.format(u))
print('dezenas:{}'.format(d))
print('centenas:{}'.format(c))
print('milhar:{}'.format(m))