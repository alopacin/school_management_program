class Educator :
    def __init__(self, name, cla):
        self.name = name
        self.cla = cla

    def __str__(self):
        return f'{self.name.capitalize()} to wychowawca klasy {self.cla}'

    def __repr__(self):
        return f" Klasa Educator(imie i nazwisko={self.name}, klasa={self.cla})"
