import random

x = str (input('digite primeiro nome'))
y = str (input('digite segundo nome'))
z = str (input('digite terceiro nome'))
a = str (input('digite quarto nome'))

lista = [x,y,z,a]

name = random.choice(lista)

ordem = (name)
print (ordem)
