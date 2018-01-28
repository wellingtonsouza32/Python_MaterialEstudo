import random
a = str(input ('digite o nome do primeiro aluno: '))
b = str(input ('digite o nome do segundo aluno: '))
c = str(input ('digite o nome do terceiro aluno: '))
d = str(input ('digite o nome do quarto aluno: '))

lista = [a,b,c,d]

r = random.choice(lista)

print(r)