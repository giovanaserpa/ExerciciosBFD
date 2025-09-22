#Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)


cliente = Cliente("Milene", "milene@email.com")
print("Nome:", cliente.nome)
print("Email:", cliente.email)

#Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")


class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)


cliente = Cliente("Lucas", "lucas@email.com")
cliente.exibir_informacoes()

#Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"


class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def saudacao(self):
        return "Olá, cliente"


usuario = Usuario("Milene", "milene@email.com")
cliente = Cliente("Lucas", "lucas@email.com")

print(usuario.saudacao())
print(cliente.saudacao())

#Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super(). com clientes arthur e milene
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"


class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente"


arthur = Cliente("Arthur", "arthur@email.com", 500)
milene = Cliente("Milene", "milene@email.com", 1000)

print("Cliente:", arthur.nome, "| Email:", arthur.email, "| Saldo:", arthur.saldo)
print("Cliente:", milene.nome, "| Email:", milene.email, "| Saldo:", milene.saldo)

#Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo


class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, setor):
        super().__init__(nome, email, cargo)
        self.setor = setor


gerente = Gerente("Maria Isabel", "misabel@email.com", "Gerente de Projetos", "TI")

print("Nome:", gerente.nome)
print("Email:", gerente.email)
print("Cargo:", gerente.cargo)
print("Setor:", gerente.setor)

#Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return "Login bem-sucedido"
        return "Falha no login"


class Permissao:
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            return "Permissão concedida"
        return "Permissão negada"


class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome


admin = Administrador("Super Admin")

print(admin.login("admin", "1234"))
print(admin.verificar_permissao("admin"))
print(admin.login("user", "wrong"))
print(admin.verificar_permissao("user"))

#Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return "Login bem-sucedido"
        return "Falha no login"

    def status(self):
        return "Status da Autenticação"


class Permissao:
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            return "Permissão concedida"
        return "Permissão negada"

    def status(self):
        return "Status da Permissão"


class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome


admin = Administrador("Super Admin")

print(admin.status())  
print(Administrador.__mro__)
