class Pessoa:
    nome = "Heliel"
    def dizerNome(self):
        print(f"Meu nome é {self.nome}")

p1 = Pessoa()

p1.dizerNome()

p2 = Pessoa()

p2.nome = "aiai"

p2.dizerNome()