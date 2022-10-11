def create_register():
    with open('class_register.txt', 'w', encoding='utf = 8') as file:
        file.write(input('Введите оценки '))


def read_register():
    with open('class_register.txt', 'r', encoding='utf = 8') as file:
        print(file.read())
