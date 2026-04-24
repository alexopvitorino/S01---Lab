from abc import ABC, abstractmethod


class Cibernetico(ABC):
    @abstractmethod
    def realizar_hack(self):
        pass


class Implante:
    def __init__(self, custo, funcao):
        self.custo = custo
        self.funcao = funcao


class NetRunner(Cibernetico):
    def __init__(self, nome, custo_implante, funcao_implante):
        self.nome = nome
        self.implante = Implante(custo_implante, funcao_implante)  

    def realizar_hack(self):
        print(f"{self.nome} executa hack [{self.implante.funcao}] | Custo: {self.implante.custo} €$")


class Faccao:
    def __init__(self, nome):
        self.nome = nome
        self.membros: list[Cibernetico] = []

    def adicionar_membro(self, membro: Cibernetico):
        self.membros.append(membro)

    def executar_todos_hacks(self):
        print(f"\n     [{self.nome}] iniciando operação     ")
        for membro in self.membros:
            membro.realizar_hack()


faccao = Faccao("Netwatch")

faccao.adicionar_membro(NetRunner("Lula", 1500, "Bolsonaro"))
faccao.adicionar_membro(NetRunner("Rhuan", 3000, "Ynogut"))
faccao.adicionar_membro(NetRunner("durval", 9999, "davi"))

faccao.executar_todos_hacks()
