import math
x = int(input('digite o cateto oposto:'))
y = int(input('digite o cateto adjacente:'))

h = math.hypot(x,y)

print ('o resultado é {}'.format(h))