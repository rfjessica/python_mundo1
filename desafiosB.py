# Rio de Janeiro, 31 de março de 2021

print('=' * 8+' Desafio 5 '+'=' * 8)
# Leia um número inteiro e mostre na tela o seu sucessor e o antecessor.
x = int((input("Digite um número: ")))
suc = x+1
ant = x-1
print('Seu valor: {} | Sucessor: {} | Antecessor: {}'.format(x, suc, ant)+'\n')

print('=' * 8+' Desafio 6 '+'=' * 8)
# Leia um número e mostre o seu dobro, triplo e raiz quadrada.
v = int(input('Digite um número: '))
d = v*2
t = v*3
r = pow(v, 1/2)
print('Seu valor: {} | Dobro: {} | Triplo: {}| Raiz Quadrada: {}'.format(v, d, t, r)+'\n')

print('=' * 8+' Desafio 7 '+'=' * 8)
# Leia as duas notas de um aluno, calcule e mostra a sua média.
nm = input('Nome do aluno? ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Notas de {}: {} e {} | Média: {}'.format(nm, n1, n2, media)+'\n')

print('=' * 8+' Desafio 8 '+'=' * 8)
# Um programa que leia um valor em metros, exibindo a conversão em centímetros e milímetros.
medida = float(input('Informe uma quantidade em metros: '))
cent = medida*100
milim = medida*1000
print('Medidas: {}m | {}cm | {}mm'.format(medida, cent, milim)+'\n')

print('=' * 8+' Desafio 9 '+'=' * 8)
# Leia um número inteiro qualquer e mostre na tela sua tabuada.
n = int(input('Insira um número inteiro: '))
ct = 0
print('#' * 8+' Tabuada de {} '.format(n)+'#' * 8)
while ct <= 10:
    print('{} x {} = {}'.format(n, ct, (n*ct)))
    ct += 1

print('\n'+'=' * 8+' Desafio 10 '+'=' * 8)
# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# (Considere 1 dólar = R$ 3,27)
r = float(input('Digite seu saldo (em R$): '))
d = r/3.27
print('Você tem R${:.2f} e pode comprar US${:.2f}'.format(r, d)+'\n')

print('=' * 8+' Desafio 11 '+'=' * 8)
# Leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.
larg = float(input('Largura da parede (em metros): '))
alt = float(input('Altura da parede (em metros) '))
areaParede = larg*alt
qTinta = areaParede/2
print('Dimensão da parede: {}mx{}m'.format(larg, alt)+' | Área da parede: {:.2f} metro(s) quadrado(s)'.format(areaParede))
print('Quantidade de tinta em litros: {}l'.format(qTinta)+'\n')

print('=' * 8+' Desafio 12 '+'=' * 8)
# Leia o preço de um produto e mostre seu novo valor, com 5% de desconto.
prc = float(input('Quanto custa o produto? '))
novo = prc-(prc*0.05)
print('Preço antigo: R${:.2f} | Valor com desconto: R${:.2f}'.format(prc, novo)+'\n')

print('=' * 8+' Desafio 13 '+'=' * 8)
# Leia o salário de um funcionário e mostre seu novo valor, com 15% de aumento.
sal = float(input('Qual é o salário? '))
reaj = sal+(sal*0.15)
print('Salário antigo: R${:.2f} | Novo salário: R${:.2f}'.format(sal, reaj)+'\n')

print('=' * 8+' Desafio 14 '+'=' * 8)
# Escreva um programa que converta uma temperatura digitada em Celsius (C) para Fahrenheit (F)
tempC = float(input('Digite uma temperatura em Celsius: '))
tempF = ((9*tempC)/5)+32
print('{}ºC corresponde a {}ºF'.format(tempC, tempF)+'\n')

print('=' * 8+' Desafio 15 '+'=' * 8)
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0.15 por km rodado.
dias = int(input('Quantos dias de aluguel? '))
km = float(input('O carro percorreu quantos quilômetros? '))
preco = (dias*60)+(km*0.15)
print('Valor do aluguel do carro que percorreu {}km, por {} dia(s): R${:.2f}'.format(km, dias, preco))
