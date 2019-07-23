#media, mediana, moda

#media
def media(lista):
	# mean(lista)
	media = sum(lista)/float(len(lista))

	return media

#mediana
def mediana(lista):
	lista_ord = sorted(lista)
	t = len(lista_ord)

	if t % 2 == 0:
		mediana = (lista_ord[int(t/2)]+lista_ord[int((t/2)-1)])/2
	else:
		mediana = lista_ord[int((t/2))]

	return mediana

#moda
def moda(lista):
	lista_dic = {}
	for l in lista:
		if l not in lista_dic:
			lista_dic[l] = 1
		else:
			lista_dic[l] += 1
	maior = max(lista_dic.values())

	for i in lista_dic:
		if lista_dic[i] == maior:
			moda = i

	return moda

