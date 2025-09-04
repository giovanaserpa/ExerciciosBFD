#Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
aluno = {
    "nome": "Giovana Serpa",
    "idade": 30,
    "nota": 9
}

#Dado o dicionário: produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
#Imprima o nome do produto e a quantidade em estoque.
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

print("Nome do produto:", produto["nome"])
print("Quantidade em estoque:", produto["estoque"])

#Dado o dicionário: carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
#Remova a chave "ano" do dicionário.
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)

#Verifique se a chave "telefone" existe no dicionário:
#contato = {"nome": "Ana", "email": "ana@email.com"}
contato = {"nome": "Ana", "email": "ana@email.com"}

if "telefone" in contato:
    print("A chave 'telefone' existe no dicionário.")
else:
    print("A chave 'telefone' NÃO existe no dicionário.")

#Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
#palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = contar_palavras(palavras)
print(resultado)

#Dado o dicionário: d = {"a": 1, "b": 2, "c": 3}
#Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in d.items()}

print(invertido)

#Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
alunos = {
    "Giovana": [7.5, 8.0, 6.5],
    "Beatriz": [9.0, 8.5, 10.0],
    "Vanessa": [6.0, 7.0, 5.5]
}
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media:.2f}")

#Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
def unir_dicionarios(dict1, dict2):
    resultado = dict1.copy()  
    resultado.update(dict2)   
    return resultado
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 4}

unido = unir_dicionarios(d1, d2)
print(unido)

#Dado o dicionário: pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
#Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
for nome, pontuacao in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
    print(f"{nome}: {pontuacao}")
