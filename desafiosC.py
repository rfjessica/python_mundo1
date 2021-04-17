# Rio de Janeiro, 9 de abril de 2021 - Aula 8: Utilizando Módulos

print('=' * 8+' Desafio 16 '+'=' * 8)
# Leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n = float(input('Digite um número: '))
print('O número digitado é {} e sua porção inteira é {}'.format(n, math.trunc(n))+'\n')

'''from math import trunc
print('O número digitado é {} e sua porção inteira é {}'.format(n, trunc(n)))

print('O número digitado é {} e sua porção inteira é {}'.format(n, int(n)))'''

print('=' * 8+' Desafio 17 '+'=' * 8)
# Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
'''hi = (co**2 + ca**2) ** (1/2)'''
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi)+'\n')

print('=' * 8+' Desafio 18 '+'=' * 8)
# Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
a = float(input('O ângulo tem quantos graus? '))
s = sin(radians(a)) # seno
print('O ângulo de {}º tem o SENO de {:.2f}'.format(a, s))
c = cos(radians(a)) # cosseno
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(a, c))
t = tan(radians(a)) # tangente
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(a, t)+'\n')

print('=' * 8+' Desafio 19 '+'=' * 8)
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('Nome escolhido: {}'.format(escolhido)+'\n')

print('=' * 8+' Desafio 20 '+'=' * 8)
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista) # embaralha os números
print('A ordem de apresntação será:', lista)

print('\n'+'=' * 8+' Desafio 21 '+'=' * 8)
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer
mixer.init()
mixer.music.load('firework.mp3')
mixer.music.play()
while mixer.music.get_busy():pass
