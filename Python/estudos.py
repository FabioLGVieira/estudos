# -*- coding: utf-8 -*-

x = 1
y = 2
""" if
print(x > y)

if(x > y):
	print('x é maior')
else:
	print('y é maior')
"""

""" elif
if x > y:
	print('x é maior')
elif x == y:
	print('são iguais')
else:
	print('y é maior')
"""

""" while

x = 0
while x <= 100:
	print (x)
	x +=10
"""

""" input 
nome = input("digite seu nome)")
print("olaaaar, " + nome)
"""

""" strings 
a = "watashi no namae wa"
b = "fabio desu @#@$ "

nome = a + " " + b
print(nome[1:]) # posicao inicial : quantas posicoes vai contar
print(nome[:9])
print(nome.strip())
frase = "o rato roeu a roupa do rei de Roma"
print(frase.split("r"))  #transforma em lista e tira o parametro da str original
print(frase.find("rei"))
print(nome.replace("fabio", "Darth Vader"))
"""
"""
def testfor():

	lista1 = [5,5,2,36,15,4,8,7]
	lista2 = ["ola ","asdas ",5]
	
	for i in lista2:
		for x in lista1:
			print(str(i) + str(x))


	for x in range(0,100):
	#print(x)
		pass

testfor()
"""

""" arquivos 

arquivo = open("arquivo.txt")

#texto = arquivo.read()  # le o arquivo todo
linha = arquivo.readline() # le uma linha do arquivo
linhas = arquivo.readlines() #le e transforma em lista     eles " deletam "  a linha do original
#print(texto)
print(linha)
print(linhas)
#for linha in linhas:
#	print(linha)
arquivo.close()

w = open("arquivo2.txt", "w")

w.write("quarta linha")
w.close()
"""

""" listas e dicionario 
lista= ["das",5, "?", 8, "batata"]
print(len(lista))

lista.append("watashi")
print(lista)

lista.remove(lista[4])
print(lista)

del lista[3]
print(lista)

del lista[:] # apaga a lista toda

if "das" in lista:
	print("tem na lista")
else:
	print("nao tem na lista")

lista2 = [ 15,20,10,30,45,23,21,8]
lista2.sort() # funciona pra ordem alfabetica tbm
print(lista2)

lista3 = sorted(lista2)

lista3.sort(reverse=True)
print(lista3)

lista3.reverse()
print(lista3)
"""

""" random

import random
numero = random.randint(7,32)
print(numero)

lista = [4,5,2,1,3,8]
numero = random.choice(lista)
print(numero)
"""

	