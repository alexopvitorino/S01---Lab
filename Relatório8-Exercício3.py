class ArmaCorpoACorpo:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def __str__(self):
        return f"{self.nome} (dano: {self.dano})"


class PhantomThieves:
    def __init__(self, nome, arma):
        self.nome = nome
        self.arma = arma

    def __str__(self):
        return f"{self.nome} | Arma: {self.arma}"


class Joker:
    def __init__(self, membros: list[PhantomThieves]):
        self.arma = ArmaCorpoACorpo("Faca Corsair", 85) 
        self.equipe = membros

    def mostrar_equipe(self):
        print(f"Joker empunha: {self.arma}")
        print("\n=== Phantom Thieves ===")
        for membro in self.equipe:
            print(membro)


equipe = [
    PhantomThieves("Ryuji Sakamoto", "Clava"),
    PhantomThieves("Ann Takamaki", "Chicote"),
    PhantomThieves("Morgana", "Cimitarra"),
]

joker = Joker(equipe)
joker.mostrar_equipe()
