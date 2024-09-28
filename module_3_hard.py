'''
Задание "Раз, два, три, четыре, пять .... Это не всё?":

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?
да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
Ученику пришлось каждый раз использовать индексацию и обращение по ключам

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):

Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов,
можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.
'''


def calculate_structure_sum(data_structure):
  summa = 0
  if isinstance(data_structure, dict):
    for key, value in data_structure.items():
      summa += calculate_structure_sum(key)
      summa += calculate_structure_sum(value)
  elif isinstance(data_structure, (list, tuple, set)):
    for item in data_structure:
      summa += calculate_structure_sum(item)
  elif isinstance(data_structure, (int, float)):
    summa += data_structure
  elif isinstance(data_structure, str):
    summa += len(data_structure)
  return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)