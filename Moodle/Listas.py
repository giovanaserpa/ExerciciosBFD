#Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["O Jantar Secreto", "O Ano da Bruxa", "A Empregada"]
print(livros)

#Usando a lista livros, exiba apenas o primeiro e o último elemento.
livros = ["O Jantar Secreto", "O Ano da Bruxa", "A Empregada"]
print("Primeiro livro:", livros[0])
print("Último livro:", livros[-1])

#Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros = ["O Jantar Secreto", "O Ano da Bruxa", "A Empregada"]
livros.append("O Segredo da Empregada") 
livros.append("Desenhos Ocultos")
print(livros)

#Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros = ["O Jantar Secreto", "O Ano da Bruxa", "A Empregada"]
livros.insert(1, "Duna")
print(livros)

#Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
livros = ["O Jantar Secreto", "O Ano da Bruxa", "A Empregada"]
livro_para_remover = "Silêncio dos inocentes"
if livro_para_remover in livros:
    livros.remove(livro_para_remover)
    print(f'Livro "{livro_para_remover}" removido.')
else:
    print("Livro não encontrado.")
print(livros)

#Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
números = [1, 2, 3, 2, 4, 2, 5]
contagem_dois = números.count(2)
print("O número 2 aparece", contagem_dois, "vezes na lista.")
print(números)

#Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
livros = ["O Jantar Secreto", "O Ano da Bruxa", "A Empregada"]
for livro in livros:
    print(f'O livro "{livro}" é interessante.')
print(livros)

#Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]
for idade in idades:    
    if idade >= 18:
        print(idade)
print(idades)

#Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma = 0
for valor in valores:
    soma += valor
print("A soma dos valores é:", soma)
print(valores)

#Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
#notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
notas = []
for i in range(2):   
    aluno_notas = []
    for j in range(3):  
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas)
print(notas)
for i, aluno_notas in enumerate(notas):
    media = sum(aluno_notas) / len(aluno_notas)
    print(f"A média do aluno {i+1} é: {media:.2f}")

#Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
#[ ] - para posições vazias, tor - para a torre, cav - para o cavalo, bis - para o bispo, rai - para a rainha, rei - para o rei, pea - para o peão.Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

import numpy as np
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]
tabuleiro[0] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[1] = ["pea"] * 8
tabuleiro[6] = ["pea"] * 8
tabuleiro[7] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro_np = np.array(tabuleiro)
for linha in tabuleiro_np:
    print(" ".join(linha))
