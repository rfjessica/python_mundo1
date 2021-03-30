#Rio de Janeiro, 30 de março de 2021.

# Faça uma função que leia algo pelo teclado e mostre na tela o seu tipo primitivo  e todas as informações possíveis sobre o valor inserido pelo usuário

print('========Desafio 4========\n')
v = input('Digite um valor: ')
print('Tipo primitivo:', type(v)) # type: função que exibe o tipo primitivo de v
print('Só tem espaços?', v.isspace())
print('É um número?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('É alfanumérico?', v.isalnum())
print('Está em maiúsculas?', v.isupper())
print('Está em minúsculas?', v.islower())
print('Está capitalizado?', v.istitle())
