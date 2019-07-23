#"""   tirar do comentario, depois que estiver funcionando
cpfn = input('Diga seu cpf(somente numeros): ')

#cpfn = 52998224725
print("seu cpf eh " + str(cpfn))

cpf = list(str(cpfn))

#for x in cpf:
print(cpf)

soma = 0
c = 10

for i in range(len(cpf)-2):
	soma += (int(cpf[i])*c)
	c-=1
dig1 = (soma*10)%11
soma = 0
c = 11
for j in range(len(cpf)-1):
	soma += (int(cpf[j])*c)
	c-=1
dig2 = (soma*10)%11

if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
	print("seu cpf é valido")
else:
	print("cpf invalido")