#100DaysOfCode, Day10,11,12
student_list = []

def create_student():
    name = input('Введите имя студента: ')
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)
    return None


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number

def print_student_details(student):
    print("{}, средняя оценка: {}.".format(student['name'],
                                         calculate_average_mark(student)))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    selection = input("Введите 'p' для выведения на экран списка студентов, \n"
                      "'s' для добавления нового студента, 'a' для добавления \n "
                      "оценки или 'q' для выхода: \n")

    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Введите ID студента, которому хотите добавить оценки: "))
            student = student_list[student_id]
            new_mark = int(input('Введите новую оценку: '))
            add_mark(student, new_mark)

        selection = input("Введите 'p' для выведения на экран списка студентов, \n"
                          "'s' для добавления нового студента, 'a' для добавления \n "
                          "оценки или 'q' для выхода: \n")

menu()
