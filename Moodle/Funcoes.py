#Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.
def saudacao():
    print("Olá, bem-vindo ao Python!")
saudacao()

#Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.
def dobro(numero):
    return numero * 2

print(dobro(2)) 

#Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.
def soma(a, b):
    return a + b
resultado = soma(10, 20)
print("O resultado da soma é:", resultado)

#Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem: "Olá, [nome]!".Caso o nome não seja informado, mostre "Olá, visitante!".
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")
mensagem("Giovana")   
mensagem()           

#Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

resultado = operacoes(10, 5)
print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])

#Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.
def media(*numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)
print("Média de 3 valores:", media(10, 20, 30))             
print("Média de 5 valores:", media(5, 10, 15, 20, 25))      
print("Média de 7 valores:", media(2, 4, 6, 8, 10, 12, 14)) 

#Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:dados_pessoais(nome="Ana", idade=25, cidade="Recife")
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")

#Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.  
def calculadora(operacao, a, b):
    def somar(x, y):
        return x + y
    def subtrair(x, y):
        return x - y
    def multiplicar(x, y):
        return x * y
    def dividir(x, y):
        if y != 0:
            return x / y
        else:
            return "Erro: divisão por zero!"
    operacoes = {
        "soma": somar,
        "subtracao": subtrair,
        "multiplicacao": multiplicar,
        "divisao": dividir
    }
    if operacao in operacoes:
        return operacoes[operacao](a, b)
    else:
        return "Operação inválida!"

print("10 + 5 =", calculadora("soma", 10, 5))
print("10 - 5 =", calculadora("subtracao", 10, 5))
print("10 * 5 =", calculadora("multiplicacao", 10, 5))
print("10 / 5 =", calculadora("divisao", 10, 5))

#Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo: def soma(a, b): return a + b aplicar_operacao(3, 4, soma)
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)
def soma(x, y):
    return x + y
def multiplicacao(x, y):
    return x * y

print(aplicar_operacao(3, 4, soma))         
print(aplicar_operacao(3, 4, multiplicacao)) 
