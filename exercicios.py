from math import sqrt
""" ex1 """

idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("voce eh maior de 18.")
else:
	print("voce nao eh maior de 18.")

""" ex2 """

nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))
media = (nota1 + nota2)/2

if media >= 6:
	print("Voce foi Aprovado")
else:
	print("Voce foi Reprovado")



""" ex3 """

print("y = x² - 1x + 6")
a = 1
b = -5
c = 6
delta = (b**2) - 4*a*c

print("Delta: " + str(delta))
if delta > 0:
	rDelta = sqrt(delta)
	raiz1 = (-b + rDelta)/2*a
	raiz2 = (-b - rDelta)/2*a
	print("raiz1: " + str(raiz1) + ", raiz2: " + str(raiz2))
elif delta == 0:
	raiz =  -b/2*a
	print("raiz: " + str(raiz))
else:
	print("Nao tem raiz real")


""" ex4 """

lista = [ 15,2,10,7 ]

for x in range(len(lista)):
	menor = 0
	maior = 0
	for i in range(len(lista)):
		if lista[x] < lista[i]:
			menor = lista[x]
			maior = lista[i]
			lista[i] = menor
			lista[x] = maior

print(lista)

""" ex5 """

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
sinal = input("digite o sinal + - / *:  ")

if sinal == "+":
	result = num1 + num2
elif sinal == "-":
	result = num1 - num2
elif sinal == "*":
	result = num1 * num2
elif sinal == "/":
	result = num1 / num2
print(result)