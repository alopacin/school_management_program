class Pupil :
    def __init__(self, name, cla):
        self.name = name
        self.cla = cla

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f" Klasa Pupil(imie i nazwisko={self.name}, klasa={self.cla})"

    def display(self, subjects, teachers):
        return f'Uczeń {self.name} uczęszcza na {subjects} prowadzone przez {teachers}'