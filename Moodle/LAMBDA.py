from functools import reduce

#dobro dos números
lista1 = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, lista1))

#filtrar pares
lista2 = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, lista2))

#soma dos números
lista3 = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, lista3)

#ordenação por comprimento da palavra
lista4 = ["uva", "banana", "maçã", "laranja"]
ordenadas_tamanho = sorted(lista4, key=lambda x: len(x))

#primeira letra maiúscula
lista5 = ["ana", "pedro", "maria"]
maiusculas = list(map(lambda x: x.capitalize(), lista5))

#produto dos números
lista6 = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, lista6)

#ordenar por último caractere
lista7 = ["banana", "uva", "maçã", "laranja"]
ordenadas_ultimo = sorted(lista7, key=lambda x: x[-1])
