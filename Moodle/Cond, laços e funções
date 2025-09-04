#1
número = int(input(print("Digite um número:")))
if número % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#2
nota = float(input("Digite uma nota de 0 a 10: "))

if nota >= 7:
   print("Aprovado.")
elif nota >= 5:
   print("Recuperação.")
else:
    print("Reprovado.")

#3
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.")

#4
idade = int(input("Digite sua idade: "))

if idade <12:
    print("Você é uma criança.")
elif idade <17:
    print("Você é um adolescente.")
elif idade <64:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

#5
nome = str(input("Digite seu nome: "))
print("Olá, " + nome + "! Seja bem-vindo(a) ao curso de Python.")

#6
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


print("=== Calculadora ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha a operação (1-4): "))

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado:", somar(a, b))
elif opcao == 2:
    print("Resultado:", subtrair(a, b))
elif opcao == 3:
    print("Resultado:", multiplicar(a, b))
elif opcao == 4:
    print("Resultado:", dividir(a, b))
else:
    print("Opção inválida!")

#7
for i in range(1, 11):
    print(i)

#8
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#9
soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    soma += numero
print(f"A soma dos números digitados é: {soma}")
