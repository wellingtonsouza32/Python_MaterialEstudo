soma = 0 #acumulador inicia com 0
cont = 0 #contador inicia com 0
for c in range (1,500,2):
    if  c % 3 == 0:
        soma += c # igual a soma = soma + c
        cont += 1 # igual a cont = cont + 1
print ("a soma dos números dividos por 3 é {} a quantidade ocorrências é {}".format(soma,cont) )

