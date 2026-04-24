from abc import ABC, abstractmethod

class Heroi(ABC):
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

    @abstractmethod
    def usar_ultimate(self):
        pass

    def __str__(self):
        return f"{self.nome} ({self.funcao})"


class Tanque(Heroi):
    def __init__(self, nome):
        super().__init__(nome, "Tanque")

    def usar_ultimate(self):
        print(f"{self.nome} ativa o ultimate de Tanque: absorve todo o dano da equipe!")


class Dano(Heroi):
    def __init__(self, nome):
        super().__init__(nome, "Dano")

    def usar_ultimate(self):
        print(f"{self.nome} ativa o ultimate de Dano: elimina todos os inimigos à vista!")


herois = [
    Tanque("Luciano"),
    Dano("Zeze"),
    Tanque("Mirosmar"),
    Dano("Di camargo"),
]

for heroi in herois:
    heroi.usar_ultimate()
