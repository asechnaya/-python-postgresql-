#100DaysOfCode Day 9.
#numbers = "5, 16, 25, 3, 4, 1"
user_input = input('Введите ваши числа, разделенные запятыми: ')
user_numbers=user_input.split(",")
user_numbers_as_int = []
for number in user_numbers:
    user_numbers_as_int.append(int(number))

#multiply each of the elements by 2 and create a list with those elements.

[number*2 for number in user_numbers]

#convert all the numbers to integers.

[int(number) for number in user_numbers]

numbers = set()
numbers.add(3)


lottery_values = {3, 5, 17, 6}
lottery_values = {3, 5, 11, 2}

lottery_values.intersection(user_values)
lottery_values.intersection(lottery_values)
