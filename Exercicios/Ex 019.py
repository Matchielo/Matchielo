# Exerício para escolher um respectivo aluno 

from random import choice

print('{:-^60}'.format(' Sorteio de Aluno '))
print('')
aluno1 = input("Qual é o nome do primeiro aluno: ")
print('')
aluno2 = input('Qual é o nome do segundo aluno: ')
print('')
aluno3 =  input('Qual é o nome do terceiro aluno: ')

lista = [aluno1, aluno2, aluno3]

print(f'''
      O  aluno sorteado foi {choice(lista)}
''')
print('')
print('{:-^60}'.format(' Fim do programa '))


