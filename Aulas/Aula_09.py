#https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=31

print('{:-^60}'.format(' Manipulação de Texto '))
print('')

frase = '  Curso em video python     '
print(frase)
print('')

# Fatiamento de Strings
print('{:*^30}'.format(' Fatiamento de Strings '))
print(frase[3])  # imprime a letra na posição 3 da frase
print(frase[3:12])  # imprime a letra da posição 3 até a posição 11 da frase
print(frase[13:])   # imprime a letra da posição 13 até o final da frase
print(frase[1:15:2])   # imprime a letra da posição 1 até a posição 14 pulando de 2
print(frase[::3])    # imprime a letra da posição 0 até o final da frase pulando de 3
print('')

# LEN -->  Tamanho da String
print('{:*^26}'.format(' Tamanho da String '))
print(len(frase))
print('')

# COUNT -->  Conta a Ocorrência de uma Letra
print('{:*^46}'.format(' Conta a Ocorrência de uma Letra/Lista '))
print(frase)
print(frase.count('o'))
print('')

# FIND -->  Encontra a Posição de uma Letra
print('{:*^40}'.format(' Encontra a Posição de uma Letra '))
print('Vai me trazer a posição da palavra *video*')
print(frase.find('video'))
print('')

# LOWER -->  Deixa a String em Minúsculo
print('{:*^36}'.format(' Deixa a String em Minúsculo '))
print(frase)
print(frase.lower())
print('')

# UPPER -->  Deixa a String em Maiúsculo
print('{:*^36}'.format(' Deixa a String em Maiúsculo '))
print(frase)
print(frase.upper())
print('')

# CAPITALIZE -->   Deixa a String com a Primeira Letra Maiúscula e o Resto em  Minúsculo
print('{:*^77}'.format(' Deixa a String com a Primeira Letra Maiúscula e o Resto em  Minúsculo '))
print(frase)
print(frase.capitalize())
print('')

# Title -->  Deixa a String com a Primeira Letra de Cada Palavra Maiúscula e o Resto em Minúsculo
print('{:*^91}'.format(' Deixa a String com a Primeira Letra de Cada Palavra Maiúscula e o Resto em Minúsculo '))
print(frase)
print(frase.title())
print('')

# REPLACE -->  Substitui uma Palavra
print('{:*^30}'.format(' Substitui uma Palavra '))
print(frase)
print(frase.replace('python','android'))
print('')

# Split -->  Divide a String em uma Lista
print('{:*^36}'.format(' Divide a String em uma Lista '))
print(frase)
lista = frase.split()
print(lista)
print(lista[2])  # Mostra a 3ª posição da lista
print(lista[2][2])   # Mostra a 3ª posição da 3ª posição da lista
print('')

# Join -->  Une uma Lista em uma String
print('{:*^36}'.format(' Une uma Lista em uma String '))
print(lista)
print('_'.join(lista))  # Une a lista com espaço
print('')

# Strip -->  Remove Espaços Excessivos no início e no final da string
print('{:*^64}'.format(' Remove Espaços Excessivos no início e no final da string '))
print(frase)
print(frase.strip())
print(len(frase.strip()))
print('')

# Rstrip -->   Remove Espaços Excessivos no final da string
# Lstrip -->  Remove Espaços Excessivos no início da string


# IN -->   Verifica se uma Palavra está Contida na String
print('{:*^54}'.format(' Verifica se uma Palavra está Contida na String '))
print('Vai verificar se a palavra *curso* está dentro da  frase')
print("Curso" in frase)
print('')