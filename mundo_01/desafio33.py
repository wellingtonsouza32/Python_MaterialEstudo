um = int(input('digite primeiro numero:'))
dois = int(input('digite segundo numero:'))
tres = int(input('digite terceiro numero:'))

# valor menor
menor = um
if tres < um and tres < dois:
    menor = tres
if dois < um and dois < tres:
    menor = dois

# Valor Maior
maior = um
if tres > um and tres > dois:
    maior = tres
if dois > um and dois > tres:
    maior = dois

print ('O maior número é {} e o menor número é {}'.format(maior,menor))