print('')
print('{:-^60}'.format(' Aluguel de Carros '))
print('')

dias = int(input('Quantos dias foram alugados: '))
print('')

km = float(input('Quantos  km foram percorridos: '))
print('')

print(f'''
    O Veículo foi alugado por {dias} dias e custou um total de R${dias*60}.
    O veículo foi percorrido por {km} km e custou um total de R$ {km*0.15}.
    O valor total do aluguel foi de R${dias*60 + km*0.15}.

''')

print('{:-^60}'.format(' Fim do programa '))
print('')