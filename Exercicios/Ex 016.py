# Exercicío para apresentar um número inteiro quando inserido um número natural
#Se as casas decimais foram menores que '0,5' arredonda para baixo, se forem maores, arredonda para cima

from math import  floor

print('')
num = float(input('Digite um número natural: '))
print('')
print(f'Seu número inteiro é {floor(num)}')