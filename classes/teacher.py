class Teacher :
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes

    def __str__(self):
        return f'{self.name.capitalize()} prowadzi klasę : {self.classes}'

    def __repr__(self):
        return f" Klasa Teacher(imie i nazwisko={self.name}, przedmiot={self.subject}, klasy={self.classes})"