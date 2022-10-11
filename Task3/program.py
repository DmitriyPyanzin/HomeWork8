from menu import main_menu as mm
from random import randint


def search():
    while True:
        n = mm()
        if n == 1:
            with open('students.csv', 'r', encoding='utf_8') as f:
                for line in f.readlines():
                    print(line)
            input('\nНажмите enter\n')

        elif n == 2:
            with open('classes.csv', 'r', encoding='utf_8') as f:
                for line in f.readlines():
                    print(line)
            input('\nНажмите enter\n')

        elif n == 3:
            with open('students.csv', 'r', encoding='utf_8') as file:
                for line in file.readlines():
                    print(line.split()[0])
            answer = input('\nВведите фамилию ученика: ').title()
            with open('students.csv', 'r', encoding='utf_8') as file:
                for line in file.readlines():
                    if answer in line:
                        print(line.split()[3])
            input('\nНажмите enter\n')

        elif n == 4:
            new_contact = input('Введите данные(ФИ, год рождения, успеваемость, ID) ').split(' ')
            with open('students.csv', 'a+', encoding='utf_8') as f:
                f.write('\n'+('\t' * 3).join(new_contact))
            input('\nНажмите enter\n')

        elif n == 5:
            with open('students.csv', 'r', encoding='utf_8') as file:
                for line in file.readlines():
                    print(line.split()[0])

            answer = input("\nВведите Фамилию: ").title()
            with open('classes.csv', 'r', encoding='utf_8') as f:
                len_random = len(f.readlines())

            cl = open('classes.csv', 'r', encoding='utf_8')
            st = open('students.csv', 'r', encoding='utf_8')
            for line in st.readlines():
                if answer in line:
                    print(cl.readlines()[randint(1, len_random-1)])
            cl.close()
            st.close()

        elif n == 6:
            print('До встречи')
            exit()
