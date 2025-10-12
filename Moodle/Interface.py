from abc import ABC, abstractmethod

# 1. Criando uma interface
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor} no cartão de crédito."

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor} no boleto."

cartao = CartaoCredito()
boleto = Boleto()
print(cartao.processar(100))
print(boleto.processar(200))

# 2. Interface múltipla
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "Computador ligado."
    def desligar(self):
        return "Computador desligado."

pc = Computador()
print(pc.ligar())
print(pc.desligar())

# 3. Interface em herança múltipla
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "Relatório impresso."
    def exportar(self):
        return "Relatório exportado."

rel = Relatorio()
print(rel.imprimir())
print(rel.exportar())

# 4. Forçando contrato
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

# class RepositorioMemoria(Repositorio):
#     def salvar(self, objeto):
#         return f"Salvando {objeto} em memória."
# repo = RepositorioMemoria()  # TypeError

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"Salvando {objeto} em memória."
    def buscar(self, id):
        return f"Buscando objeto com id {id}."

repo = RepositorioMemoria()
print(repo.salvar("dados"))
print(repo.buscar(1))
