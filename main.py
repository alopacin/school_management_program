#importowanie modulow klas
from classes.pupil import Pupil
from classes.teacher import Teacher
from classes.educator import Educator

# utworzenie slownikow
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
            break
        elif inquiry == 'uczeń' or inquiry == 'uczen':
            pupil_name = input('Podaj imię i nazwisko ucznia: ')
            pupil_class = input('Podaj do jakiej klasy chodzi uczeń: ')
            new_student = Pupil(pupil_name, pupil_class)
            student_list.append(new_student)
            classes_list.append(pupil_class)
        elif inquiry == 'nauczyciel':
            teacher_name = input('Podaj imię i nazwisko nauczyciela: ')
            teacher_subject = input('Podaj nazwę przedmiotu, który prowadzi nauczyciel: ')
            while True:
                teacher_class = input('Podaj klasę/y, które prowadzi nauczyciel: ')
                if teacher_class == '':
                    break
                classes_list.append(teacher_class)
                new_teacher = Teacher(teacher_name, teacher_subject, teacher_class)
        elif inquiry == 'wychowawca':
            educator_name = input('Podaj imię i nazwisko wychowawcy: ')
            educator_class = input('Podaj klasę jaką prowadzi wychowawca: ')
            new_educator = Educator(educator_name, educator_class)
            classes_list.append(educator_class)
            educator_list.append(new_educator)
        elif inquiry == 'koniec':
            break

# czesc programu odpowiadajaca za zarzadzanie uzytkownikami
    elif ask == 'zarządzaj' or ask == 'zarzadzaj':
        conditionsss = ['klasa', 'uczeń', 'uczen', 'nauczyciel', 'wychowawca']
        inquiry = input('Wybierz następującą opcję: \nklasa\nuczeń\nnauczyciel\nwychowawca\nkoniec\n')
        if inquiry not in conditionsss :
            print('Spróbuj jeszcze raz')
            break
        elif inquiry == 'klasa':
            choice = input('Wpisz nazwę klasy: ')
            if choice not in classes_list:
                print('Nie ma takiej klasy')
                continue
            else:
                print('Lista uczniów:')
                for student in student_list:
                    if student.cla == choice :
                        print(student)
                for educator in educator_list:
                    if educator.cla == choice :
                        print(educator)
        elif inquiry == 'uczen' or inquiry == 'uczeń':
            choice = input('Podaj imię i nazwisko ucznia ')
            for student in student_list:
                if student.name == choice:
                    pass



        elif inquiry == 'nauczyciel':



        elif inquiry == 'wychowawca':
            choice = input('Wpisz imię i nazwisko wychowawcy ')
            for educator in educator_list:
                if educator.name == choice:
                    x = educator.cla
                    for student in student_list:
                        if student.cla == x:
                            print(student)

        elif inquiry == 'koniec':
            break
    elif ask == 'koniec':
        break
