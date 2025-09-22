#Exercício 1: Crie uma lista com diferentes tipos de dados e imprima-a.
lista_mista = ["Giovana", 25, 3.14, True, [1, 2, 3], {"chave": "valor"}]
print(lista_mista)

#Exercício 2: Adicione, remova e modifique elementos na lista criada no exercício 1.
lista_mista = ["Giovana", 25, 3.14, True, [1, 2, 3], {"chave": "valor"}]
lista_mista.append("Python")         # adiciona no final da lista
lista_mista.insert(2, 99)            # insere o número 99 na posição 2
lista_mista.remove(True)             # remove o valor True da lista
print(lista_mista)

#Exercício 3 e 4: Crie uma cópia da lista do exercício 1 e verifique se são a mesma lista ou listas diferentes.
lista_mista = ['Giovana', 25, 99, 3.14, [1, 2, 3], {'chave': 'valor'}, 'Python']
lista_copia = lista_mista.copy()
print("ID da lista original:", id(lista_mista))
print("ID da cópia:", id(lista_copia))
if id(lista_mista) == id(lista_copia):
    print("É a mesma lista!")
else:
    print("São listas diferentes!")

#Exercício 5: Crie uma lista de números e utilize uma compreensão de lista para criar uma nova lista com os números multiplicados por 5.
numeros = [2, 4, 6.5, 10, 3.2]
numeros_mult = [num * 5 for num in numeros]
print("Lista original:", numeros)
print("Lista multiplicada:", numeros_mult)

#Exercício 6: Crie uma lista de números e utilize fatiamento para criar uma nova lista com os elementos do índice 3 ao 5.
lista = [1, 2, 3, 4, 5, 6]
nova_lista = lista[3:5]
print("Nova lista:", nova_lista)
