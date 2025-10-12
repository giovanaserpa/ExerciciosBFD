# 1. Associação Pessoa e Livro
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

p = Pessoa("Ana")
l = Livro("Python Básico")
p.livro = l
print(p.nome, "está lendo", p.livro.titulo)

# 2. Associação Aluno e Onibus
class Onibus:
    def __init__(self, linha):
        self.linha = linha

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def pegar_onibus(self, onibus):
        return f"{self.nome} pegou o ônibus {onibus.linha}"

a = Aluno("João")
o = Onibus("101")
print(a.pegar_onibus(o))

# 3. Agregação Departamento e Funcionário
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

f1 = Funcionario("Carlos")
f2 = Funcionario("Maria")
d = Departamento("TI")
d.adicionar_funcionario(f1)
d.adicionar_funcionario(f2)
print([f.nome for f in d.funcionarios])

# 4. Agregação Time e Jogador
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

t = Time("Brasil")
j1 = Jogador("Neymar", "Atacante")
j2 = Jogador("Alisson", "Goleiro")
t.adicionar_jogador(j1)
t.adicionar_jogador(j2)
print([j.nome for j in t.jogadores])

# 5. Composição Carro e Motor
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

c = Carro("Fusca", 1300)
print(c.modelo, c.motor.potencia)
del c

# 6. Composição Casa e Comodo
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [Comodo("Sala"), Comodo("Cozinha"), Comodo("Quarto")]

casa = Casa()
print([c.nome for c in casa.comodos])
