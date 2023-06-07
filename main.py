class Pupil :
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def pupil_information(self):
        pass



class Teacher :
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Educator :
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


conditions = ('utwórz', 'utworz', 'zarządzaj', 'zarzadzaj', 'koniec')
while True:
    ask = input('Co chcesz zrobić (utwórz, zarządzaj, koniec)?: ')
    if ask not in conditions:
        print('Podałeś nieprawidłową komendę.Spróbuj jeszcze raz')
        continue
    elif ask == 'utwórz' or ask == 'utworz':
        conditionss = ('uczeń', 'uczen', 'nauczyciel', 'wychowawca', 'koniec')
        inquiry = input('Wybierz następującą opcję: \nuczeń\nnauczyciel\nwychowawca\nkoniec\n')
        if inquiry not in conditionss:
            print('Spróbuj jeszcze raz')
            break
        elif inquiry == 'uczeń' or inquiry == 'uczen':
            pupil_name = input('Podaj imię ucznia: ')
            pupil_lastname = input('Podaj nazwisko ucznia: ')
            pupil_class = input('Podaj do jakiej klasy chodzi uczeń: ')
            new_pupil = Pupil(pupil_name, pupil_lastname)
            new_pupil.pupil_information()


            pass
        elif inquiry == 'nauczyciel':

            pass
        elif inquiry == 'wychowawca':

            pass
        elif inquiry == 'koniec':
            break

    elif ask == 'zarządzaj' or ask == 'zarzadzaj':

        pass


    elif ask == 'koniec':
        break
