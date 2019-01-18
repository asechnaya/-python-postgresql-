#100DaysOfCode, Day10,11

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


'''
import sys
my_vars = []
for i in range(3):
    my_vars.append(lambda: i)
#print([f() for f in my_vars])
print(sys.argv)

'''