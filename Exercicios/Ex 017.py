# Exercício para calcular a hipotenhusa de um triângulo retangulo

import math

print('')
print('{:-^60}'.format(' Calculo da Hipotenusa  '))
print('')
cateto_adjacente = float(input('Digite o valor do Cateto Adjacente: '))
print('')
cateto_oposto = float(input('Digite o valor do Cateto Oposto: '))
print('')
# hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)
# print(f'A hipotenusa do triângulo retângulo é {hipotenusa:.2f}.')

hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print(f'A hipotenusa do triângulo retângulo é {hipotenusa:.2f}.')
print('')  # espaço em branco para melhorar a visualização.
print('{:-^60}'.format(' FIM DO PROGRAMA '))  # linha de igual ação para melhorar a visualização.  # noqa: E501
