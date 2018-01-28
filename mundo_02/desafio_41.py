a = int(input('digite a idade'))

if a <= 9:
    print('Mirim')
elif a > 9 and a <= 14:
    print('infantil')
elif a > 14 and a <= 19:
    print('junior')
elif a > 19 and a <= 20:
    print('Sênior')
else:
    print('Master')
