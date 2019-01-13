import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]

def ask_user_and_check():
    user_number = int(input("Введите число от 0 до 9: "))
    if user_number in magic_numbers:
        return "Вы угадали число!"
    if user_number not in magic_numbers:
        return 'Вы даже не близко.'

def run_program_x_times(chances):
    for attempt in range(chances):#range(chances) is [0, 1, 2]
        print('Это попытка номер {}'.format(attempt))
        message = ask_user_and_check()
        print(message)

user_attempts = int(input('Введите количество попыток: '))        
run_program_x_times(2)

'''    
minimum=100
for index in range(10):
    random_number=random.randint(0,100)
    print('Сгенерированное число {}'.format(random_number))
    if random_number < minimum:
            minimum = random_number
print('minumum {}'.format(minimum))
'''
        
