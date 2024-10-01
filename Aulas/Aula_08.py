# Aula para desenvolvimento de aprendizagem de bibliotecas

import math #  Importa a biblioteca math
import random

print('')
num = random.random()
num2 = random.randint(1, 100) #  Gera um número aleatório entre 1 e 100

print('')
print(f'Analisando o número aleatório_1 de 0 a 1: {num}...')

raiz = math.sqrt(num)  # Calcula a raiz quadrada do número

print(f'''
      
    A raiz quadrada de {num} é {raiz:.2f},
    Arredondando o valor para cima {math.ceil(raiz)} ou para baixo {math.floor(raiz)},

''')

print(f'Analisando o número aleatório_2 de 1 a 100: {num2}...')
raiz = math.sqrt(num2)  # Calcula a raiz quadrada do número

print(f'''
      
    A raiz quadrada de {num2} é {raiz:.2f},
    Arredondando o valor para cima {math.ceil(raiz)} ou para baixo {math.floor(raiz)},

''')
