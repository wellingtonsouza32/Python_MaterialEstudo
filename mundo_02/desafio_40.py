from time import sleep
print('Calculo de notas')
sleep(5)

a = float(input('Digite primeira nota:'))
b = float(input('digite segunda nota'))

nota = (a + b) / 2

if nota >= 7:
    print ('aprovado')
elif nota < 5:
    print ('reprovado')
else:
    print('recuperação')