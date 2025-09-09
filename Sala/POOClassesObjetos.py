#Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
   
pessoa1 = pessoa ("Giovana", 30)
pessoa2 = pessoa ("Rose", 64)
print(f"Pessoa 1: Nome = {pessoa1.nome}, Idade = {pessoa1.idade}")
print(f"Pessoa 2: Nome = {pessoa2.nome}, Idade = {pessoa2.idade}")

#Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = pessoa ("João", 25)
pessoa1.apresentar()

#Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
carro1 = Carro ("Kardian", "Renault", 2025)
carro2 = Carro ("Kicks", "Nissan", 2025)
carro3 = Carro ("Renegade", "Land Rover", 2023)

carro1.mostrar_informacoes()
carro2.mostrar_informacoes()
carro3.mostrar_informacoes()

#Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
carromainha = Carro ("Kardian", "Renault", 2025)
carromainha.mostrar_informacoes()

carromainha.ano = 2024
carromainha.mostrar_informacoes()

#Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo restante: R${self.saldo:.2f}")
conta = ContaBancaria("Carlos", 1000)
conta.depositar(500)    
conta.sacar(200)        
conta.sacar(1500)       
conta.depositar(-50)    
conta.sacar(-100)      

#Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
            return False
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo restante: R${self.saldo:.2f}")
            return True

conta = ContaBancaria("Giovana", 1000)

if conta.sacar(200):
    print("Saque efetuado com sucesso!")
else:
    print("Falha ao tentar sacar.")

if conta.sacar(1500):
    print("Saque efetuado com sucesso!")
else:
    print("Falha ao tentar sacar.")

#Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

aluno1 = Aluno("Giovana", 8.5)
aluno2 = Aluno("Arthur", 7.0)
aluno3 = Aluno("Vitoria", 9.2)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

print("Alunos da turma:")
turma.listar_alunos()

#Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

aluno1 = Aluno("Giovana", 9.5)
aluno2 = Aluno("Bruno", 7.8)

print(aluno1)
print(aluno2)

#Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.
class Cachorro:
    especie = "Canis familiaris"  
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

dog = Cachorro("Meg", 12)

print("Acesso pelo nome da classe:", Cachorro.especie)
print("Acesso pelo objeto:", dog.especie)

print(f"Nome do cachorro: {dog.nome}")
print(f"Idade do cachorro: {dog.idade}")
