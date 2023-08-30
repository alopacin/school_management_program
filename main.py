#importowanie modulow klas
from classes.pupil import Pupil
from classes.teacher import Teacher
from classes.educator import Educator

# utworzenie list
student_list = []
teacher_list = []
educator_list = []
classes_list = []

conditions = ('utwórz', 'utworz', 'zarządzaj', 'zarzadzaj', 'koniec')
while True:
    ask = input('Co chcesz zrobić (utwórz, zarządzaj, koniec)?: ')
    if ask not in conditions:
        print('Podałeś nieprawidłową komendę.Spróbuj jeszcze raz')
        continue

# czesc programu odpowiadajaca za proces tworzenia uzytkownikow
    elif ask == 'utwórz' or ask == 'utworz':
        conditionss = ('uczeń', 'uczen', 'nauczyciel', 'wychowawca', 'koniec')
        inquiry = input('Wybierz następującą opcję: \nuczeń\nnauczyciel\nwychowawca\nkoniec\n')
        if inquiry not in conditionss:
            print('Spróbuj jeszcze raz')
            continue

# dodawanie do listy ucznia
        elif inquiry == 'uczeń' or inquiry == 'uczen':
            pupil_name = input('Podaj imię i nazwisko ucznia: ')
            pupil_class = input('Podaj do jakiej klasy chodzi uczeń: ')
            new_student = Pupil(pupil_name, pupil_class)
            student_list.append(new_student)
            if pupil_class not in classes_list:
                classes_list.append(pupil_class)

# dodawanie do listy nauczyciela
        elif inquiry == 'nauczyciel':
            teacher_name = input('Podaj imię i nazwisko nauczyciela: ')
            teacher_subject = input('Podaj nazwę przedmiotu, który prowadzi nauczyciel: ')
            new_teacher = Teacher(teacher_name, teacher_subject)
            teacher_list.append(new_teacher)
            while True:
                teacher_class = input('Podaj klasę/y, które prowadzi nauczyciel: ')
                if teacher_class == '':
                    break
                new_teacher.add_class(teacher_class)
                if teacher_class not in classes_list:
                    classes_list.append(teacher_class)

# dodawanie do listy wychowawcy
        elif inquiry == 'wychowawca':
            educator_name = input('Podaj imię i nazwisko wychowawcy: ')
            educator_class = input('Podaj klasę jaką prowadzi wychowawca: ')
            new_educator = Educator(educator_name, educator_class)
            educator_list.append(new_educator)
            if educator_class not in classes_list:
                classes_list.append(educator_class)

        elif inquiry == 'koniec':
            continue

# czesc programu odpowiadajaca za zarzadzanie uzytkownikami
    elif ask == 'zarządzaj' or ask == 'zarzadzaj':
        conditionsss = ['klasa', 'uczeń', 'uczen', 'nauczyciel', 'wychowawca']
        inquiry = input('Wybierz następującą opcję: \nklasa\nuczeń\nnauczyciel\nwychowawca\nkoniec\n')
        if inquiry not in conditionsss :
            print('Spróbuj jeszcze raz')
            continue

# wyswietlenie listy uczniow i wychowawcy wpisanej przez uzytkownika klasy
        elif inquiry == 'klasa':
            choice = input('Wpisz nazwę klasy: ')
            if choice not in classes_list:
                print('Nie ma takiej klasy')
                continue
            else:
                print('Lista uczniów:')
                for pupil in student_list:
                    if pupil.cla == choice :
                        print(pupil)
                for educator in educator_list:
                    if educator.cla == choice :
                        print(educator)

# wyswietlenie przedmiotow na ktore uczeszcza wpisany uczen i ich nauczycieli
        elif inquiry == 'uczen' or inquiry == 'uczeń':
            choice = input('Podaj imię i nazwisko ucznia ')
            student_found = False
            for student in student_list:
                if student.name == choice:
                    student_found = True
                    has_lessons = False
                    for teacher in teacher_list:
                        if student.cla in teacher.classes:
                            has_lessons = True
                            print(student.display(teacher.subject, teacher.name))
                    if not has_lessons:
                        print('Uczeń nie ma żadnych lekcji')
            if not student_found:
                print('Nie ma takiego ucznia')

# wyswietlenie wpisanego nauczyciela i klasy jakie naucza
        elif inquiry == 'nauczyciel':
            choice = input('Podaj imię i nazwisko nauczyciela: ')
            teacher_found = False
            for teacher in teacher_list:
                if teacher.name == choice:
                    teacher_found = True
                    print(teacher)
            if not teacher_found:
                print('Nie ma takiego nauczyciela')

# wyswietlenie uczniow, ktorych wpisany wychowawca jest wychowawca
        elif inquiry == 'wychowawca':
            choice = input('Wpisz imię i nazwisko wychowawcy ')
            educator_found = False
            for educator in educator_list:
                if educator.name == choice:
                    educator_found = True
                    x = educator.cla
                    for student in student_list:
                        if student.cla == x:
                            print(f'Lista uczniów:\n{student}')
            if not educator_found:
                print('Nie ma takiego wychowawcy')

        elif inquiry == 'koniec':
            continue

# jezeli zostanie wpisany koniec, program konczy dzialanie
    elif ask == 'koniec':
        break
