import media as m
import aleatorio as a

lista = a.geraLista(6)
print(lista)

media = m.media(lista)
print("media: " + str(media))

mediana = m.mediana(lista)
print("mediana: " + str(mediana))

moda = m.moda(lista)
print("moda: " + str(moda))