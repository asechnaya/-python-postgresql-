#100DaysOfCode, Day10
#sample_set = {3, 5, 9, 1, 1}

student= {'имя':'Jose',
          'оценки':[0,67,80,44,100],
          "экзамены": {
              'final':60,
              'midterm':50
          }}
#print(student['mark'][1])
print(student['экзамены']['final'])

def create_student():
    name = input('Введите имя студента: ')
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data

print(create_student())