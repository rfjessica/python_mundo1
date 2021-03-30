#Rio de Janeiro, 29 de março de 2021.

#Aula 4 – Primeiros comandos em Python3

#Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas, de acordo com o valor digitado
print('========Desafio 1========')
nome = input('Qual é o seu nome? ')
print('Olá, ', nome, '! Prazer em te conhecer!')

#Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
print('\n========Desafio 2========')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Você nasceu no dia ', dia, 'de', mes, 'de', ano,', correto?')

#Crie um script que leia dois números e tente mostrar a soma entre eles
print('\n========Desafio 3========')
x = input('Primeiro número: ')
y = input('Segundo número: ')
soma = int(x)+int(y) #Preciso converter x e y para o tipo inteiro
print('A soma de', x, 'e', y, 'é:', str(soma)) #Agora, imprimo o resultado como uma string
