# Exercicio para calcular o angulo desejado em seno, cosseno e tangente
from math import sin,cos, tan, radians

print('{:-^60}'.format(' Calculo do ângulo  desejado '))
print('')
angulo = float(input('Digite o ângulo desejado em graus: '))   

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'''
    O ângulo digitado é {angulo}

    O seno é {seno:.2f}
    O cosseno é {cosseno:.2f}
    A tangente é {tangente:.2f}
''')

print('{:-^60}'.format(' Fim do programa '))  # Imprime uma linha

