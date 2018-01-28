cont = 0
res = 0
p = int(input('Digite o primeiro termo'))
r = int(input('Digite a razão'))

for cont in range(0,11):
    cont += 1
    res += r
    if cont <= 10:
        print(res)