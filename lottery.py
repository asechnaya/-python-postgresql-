#100DaysOfCode Day 9.
import random

def menu():
    # Просит пользователя ввести числа
    user_numbers = get_player_numbers()
    # Вычисление чисел ля лотереи
    lottery_numbers = create_lottery_numbers()
    # Выводит выигрышные номера
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print('Совпадающие числа: {}. Вы выиграли ${}!'.format(matched_numbers,100 ** len(matched_numbers)))



# Пользователь может выборать 6 чисел.
def get_player_numbers():
    number_csv = input('Введите ваши 6 чисел, разделенных запятыми: ')
    #создание множества целых числе из number_csv
    number_list = number_csv.split(',')
    integer_set = {int(number) for number in number_list}
    return integer_set

# Лотерея генерирует 6 случайных чисел (от 1 до 20).

def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(0,20))
    return values

'''
Сопоставляются введеные пользователем числа и числа из лотереи.
Выигрыш основан на количестве совпавших чисел
'''

menu()
