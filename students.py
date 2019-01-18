#100DaysOfCode, Day10,11
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

s = create_student()
print(calculate_average_mark(s))
add_mark(s, 63)
print(calculate_average_mark(s))
add_mark(s, 3)
print(calculate_average_mark(s))


def print_student_details(student):
    print("{}, средняя оценка: {}".format(students['name'],
                                          calculate_average_mark(student)))

def print_student_list(students):
    for student in students:
        print_student_details(student)

'''
import sys
my_vars = []
for i in range(3):
    my_vars.append(lambda: i)
#print([f() for f in my_vars])
print(sys.argv)

'''