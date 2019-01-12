import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]
chance = 3
for attempt in range(chance):
    print('Это попытка номер {}'.format(attempt))
    user_number = int(input("Введите число от 0 до 9: "))
    if user_number in magic_numbers:
        print("Вы угадали число!")
    if user_number not in magic_numbers:
        print('Вы даже не близко.')


minimum=100
for index in range(10):
    random_number=random.randint(0,100)
    print('Сгенерированное число {}'.format(random_number))
    if random_number < minimum:
            minimum = random_number
print('minumum {}'.format(minimum))
        
