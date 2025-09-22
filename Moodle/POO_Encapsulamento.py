#Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)
class ContaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo if saldo >= 0 else 0

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo")


conta = ContaBancaria(100)
print("Saldo inicial:", conta.get_saldo())
conta.set_saldo(200)
print("Saldo atualizado:", conta.get_saldo())
conta.set_saldo(-50)
print("Saldo final:", conta.get_saldo())

#Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, identidade):
        self.__identidade = identidade


pessoa = Pessoa("Arthur", "27/05/1998", "123.456.789-00", "MG-12.345.678")
print("Nome:", pessoa.nome)
print("Data de nascimento:", pessoa.data_nascimento)
print("CPF:", pessoa.get_cpf())
print("Identidade:", pessoa.get_identidade())

pessoa.set_cpf("987.654.321-00")
pessoa.set_identidade("SP-98.765.432")
print("Novo CPF:", pessoa.get_cpf())
print("Nova identidade:", pessoa.get_identidade())
