#importowanie modulow klas
from classes.pupil import Pupil
from classes.teacher import Teacher
from classes.educator import Educator

#tworzenie slownikow
student_list = []
teacher_list = []
educator_list = []

conditions = ('utwórz', 'utworz', 'zarządzaj', 'zarzadzaj', 'koniec')
while True:
    for student in student_list:
        print(student)
    print(educator_list)
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
            new_student = Pupil(pupil_name, pupil_class)
            student_list.append(new_student)
        elif inquiry == 'nauczyciel':
            teacher_name = input('Podaj imię i nazwisko nauczyciela: ')
            teacher_subject = input('Podaj nazwę przedmiotu, który prowadzi nauczyciel: ')
            while True:
                teacher_class = input('Podaj klasę/y, które prowadzi nauczyciel: ')
                if teacher_class == '':
                    break
                new_teacher = Teacher(teacher_name, teacher_subject, teacher_class)
        elif inquiry == 'wychowawca':
            educator_name = input('Podaj imię i nazwisko wychowawcy: ')
            educator_class = input('Podaj klasę jaką prowadzi wychowawca: ')
            new_educator = Educator(educator_name, educator_class)
            educator_list.append(new_educator)
        elif inquiry == 'koniec':
            break

#czesc programu odpowiadajaca za zarzadzanie uzytkownikami
    elif ask == 'zarządzaj' or ask == 'zarzadzaj':
        conditionsss = ['klasa', 'uczeń', 'uczen', 'nauczyciel', 'wychowawca']
        inquiry = input('Wybierz następującą opcję: \nklasa\nuczeń\nnauczyciel\nwychowawca\nkoniec\n')
        if inquiry not in conditionsss :
            print('Spróbuj jeszcze raz')
            break
        elif inquiry == 'klasa':
            pass


        elif inquiry == 'uczen' or inquiry == 'uczeń':
            pass


        elif inquiry == 'nauczyciel':
            pass


        elif inquiry == 'wychowawca':
            pass


        elif inquiry == 'koniec':
            break
    elif ask == 'koniec':
        break
