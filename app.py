#100DaysOfCode, Day10,11
#100DaysOfCode, Day10,11,12
student_list = []

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0

        total = sum(self.marks)
        return total / number



def create_student():
    name = input('Введите имя студента: ')
    student_data = Student(name)

    return student_data


def add_mark(student, mark):
    student.marks.append(mark)
    return None


def print_student_details(student):
    print("{}, средняя оценка: {}.".format(student.name,
                                         student.average_mark()))


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

'''
import sys
my_vars = []
for i in range(3):
    my_vars.append(lambda: i)
#print([f() for f in my_vars])
print(sys.argv)

'''