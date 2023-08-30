class Teacher :
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.classes = []

    def __str__(self):
        return f'{self.name.capitalize()} prowadzi klasę/y : {", ".join(self.classes)}'

    def __repr__(self):
        return f" Klasa Teacher(imie i nazwisko={self.name}, przedmiot={self.subject}, klasy={self.classes})"

    def add_class(self, cla):
        self.classes.append(cla)
