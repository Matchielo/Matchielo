# Sorteia a ortem de uma lista

from random import shuffle

print('{:-^60}'.format(' Ordem de apresentação '))
print('')
a1 =  str(input('Primeiro aluno: '))
a2 =  str(input('Segundo aluno: '))
a3 =  str(input('Terceiro aluno: '))
a4 =  str(input('Quarto aluno: '))

sorteio = [a1,a2,a3,a4]
shuffle(sorteio)

print(f'''
    A odem de apresentação é:
    {sorteio}
''')
print('{:-^60}'.format(' Fim do programa '))
