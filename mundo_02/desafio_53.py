
p = str(input('Digite uma frase e descubra se ela é um palindromo!')).strip()
resultado = []
for palavra in p: #O for vai colocar em palavra cada caractere da string que está em p, da esquerda para a direita até o final da string.
    temp = '' # inclui a figura do temp que separará letra a letra
    for letra in palavra: # letras dentro de palavra
            temp += letra
    resultado.append(temp) #append está incluindo temp dentro da lista resultado para fazer o tratamento abaixo
    print (resultado)
    c = resultado[::-1] #tratamento do resultado o valor -1 está invertendo o texto
if c == resultado: # if esta comparando o texto para saber letra por letra se é igual
    print ('é palindromo')
else:
    print ('não é palindromo')
print (resultado)