# Rio de Janeiro, 10 de abril de 2021 -  Aula 9: Manipulando Texto
'''Desafio 22: leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas
* O nome com todas as minúsculas
* Quantidade de letras (sem considerar espaços)
* Quantidade de letras do primeiro nome'''
print('\n'+'=' * 8+' Desafio 22 '+'=' * 8)
nome = str(input('Nome completo? ')).strip()
print('Em MAIÚSCULAS: '+format(nome.upper()))
print('Em minúsculas: '+format(nome.lower()))
lista = nome.split()
primeiro = lista[0]
print('Quantidade de letras (sem considerar espaços): {}'.format(len(nome)-nome.count(' ')))
print('Quantidade de letras do primeiro nome ({}): {}'.format(primeiro, len(lista[0])))

'''Desafio 23: leia um número de 0 a 9999 e mostre na tela cada dígito separado.
Exemplo:
Digite um número: 1834
unidade: 4 | dezena: 3 | centena: 8 | milhar: 1'''
print('\n'+'=' * 8+' Desafio 23 '+'=' * 8)
num = int(input('Digite um número entre 0 e 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('Você digitou o número {}'.format(num))
print('Milhar: {} | Centena: {} | Dezena: {} | Unidade: {}'.format(m, c, d, u))

'''D 24: leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"'''
print('\n'+'=' * 8+' Desafio 24 '+'=' * 8)
cidade = str(input('Qual é o nome da cidade? '))
res = cidade.startswith('Santo')
if(res == True): print('A cidade começa com "Santo"')
else: print('A cidade não começa com "Santo"')

#D 25: leia o nome de uma pessoa e diga se ela tem "Silva" no nome
print('\n'+'=' * 8+' Desafio 25 '+'=' * 8)
nome = str(input('Nome completo? '))
print('Silva' in nome)

'''d 26: leia uma frase pelo teclado e mostre '''
print('\n'+'=' * 8+' Desafio 26 '+'=' * 8)
frase = str(input('Escreva uma frase aqui: '))
print('A letra A aparece {} vezes.'.format(frase.count('A'))) #quantas vezes aparece a letra "A"
print('Primeiro índice em que a letra A foi encontrada'.format(frase.find('A'))) #em qual posição a letra "A" aparece pela 1ª vez
print(frase.rindex('A')) #em qual posição a letra "A" aparece pela última vez

'''d 27: leia o nome completo de uma pessoa e mostre o PRIMEIRO NOME e o ÚLTIMO NOME separadamente'''
print('\n'+'=' * 8+' Desafio 27 '+'=' * 8)
nome = str(input('Nome completo? '))
lista = nome.split()
print('Primeiro nome: {}'.format(lista[0]))
print('Último nome: {}'.format(lista[len(lista)-1]))
