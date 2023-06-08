#importowanie modulow klas
from classes.pupil import Pupil
from classes.teacher import Teacher
from classes.educator import Educator

#tworzenie slownikow
student_list = {}
teacher_list = {}
educator_list = {}

conditions = ('utwórz', 'utworz', 'zarządzaj', 'zarzadzaj', 'koniec')
while True:
    print(student_list)
    ask = input('Co chcesz zrobić (utwórz, zarządzaj, koniec)?: ')
    if ask not in conditions:
        print('Podałeś nieprawidłową komendę.Spróbuj jeszcze raz')
        continue

#czesc programu odpowiadajaca za proces tworzenia uzytkownikow
    elif ask == 'utwórz' or ask == 'utworz':
        conditionss = ('uczeń', 'uczen', 'nauczyciel', 'wychowawca', 'koniec')
        inquiry = input('Wybierz następującą opcję: \nuczeń\nnauczyciel\nwychowawca\nkoniec\n')
        if inquiry not in conditionss:
            print('Spróbuj jeszcze raz')
            break
        elif inquiry == 'uczeń' or inquiry == 'uczen':
            pupil_name = input('Podaj imię i nazwisko ucznia: ')
            pupil_class = input('Podaj do jakiej klasy chodzi uczeń: ')
            new_student = Pupil(pupil_name)
            student_list[new_student] = pupil_class
        elif inquiry == 'nauczyciel':
            teacher_name = input('Podaj imię i nazwisko nauczyciela: ')
            teacher_subject = input('Podaj nazwę przedmiotu, który prowadzi nauczyciel: ')
            teacher_class = input('Podaj klasę/y, które prowadzi nauczyciel: ')
            new_teacher = Teacher(teacher_name)
            teacher_list[new_teacher] = teacher_subject, teacher_class
        elif inquiry == 'wychowawca':
            educator_name = input('Podaj imię i nazwisko wychowawcy: ')
            educator_class = input('Podaj klasę jaką prowadzi wychowawca: ')
            new_educator = Educator(educator_name)
            educator_list[new_educator] = educator_class
        elif inquiry == 'koniec':
            break
#czesc programu odpowiadajaca za zarzadzanie uzytkownikami
    elif ask == 'zarządzaj' or ask == 'zarzadzaj':

        pass


    elif ask == 'koniec':
        break
