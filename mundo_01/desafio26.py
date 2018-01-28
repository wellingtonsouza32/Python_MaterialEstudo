f = str(input('Digite a Frase:')).upper()
print ('A frase contém {} letra(s) A'.format(f.count('A')))
print ('A posição da primeira letra A é {}'.format(f.find('A')+1))
print ('A posição da última letra A é {}'.format(f.rfind('A')+1))
