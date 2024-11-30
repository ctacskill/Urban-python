def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    correct_data = 0
    for i in numbers:
        try:
            result += i
            correct_data += 1
        except TypeError:
            print(f'неккоректный тип данных {i}')
            incorrect_data += 1
    return (result, incorrect_data, correct_data)

def calculate_average(numbers):
    try:
        sum_ = personal_sum(numbers)
        try:
            return sum_[0] / sum_[2]
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
