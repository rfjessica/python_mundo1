frase = 'Curso em Vídeo Python'
print(frase)
print(len(frase))

print(frase[3])
print(frase[3:13]) # do quarto caracter até a posição 12
print(frase[:13]) # do início até a posição 12
print(frase[13:]) # da posição 13 até o final
print(frase[1:15]) # do 2º caracter até a posição 14
print(frase[1:15:2]) # do 2º caracter até a posição 14, pulando de 2 em 2
print(frase[1::2]) # desde o 2º caracter, pulando de 2 em 2, até o fim
print(frase[::2]) # pulando de 2 em 2 (não definimos o início nem o fim)

print("""Welcome! Are you completely new to programming? 
If not then we presume you will be looking for information about why and how to get 
started with Python. Fortunately an experienced programmer in any programming language 
(whatever it may be) can pick up Python very quickly. 
It's also easy for beginners to use and learn, so jump in!""")

print(frase.capitalize())
print(frase.title())
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.replace('Python', 'Android'))
'''A string é imutável, com exceção deste caso:
frase = frase.replace('Python', 'Android')
print(frase)'''

print('Curso' in frase)
print(frase.find('Vídeo')) #indica a posição inicial da string (palavra não correspondida: retorna -1)
print(frase.split()) #divide a frase

dividido = frase.split()
print(dividido[0]) #mostra o 1º elemento da lista
print(dividido[2][3]) #mostra o conteúdp no índice 3 do 2º elemento da lista
