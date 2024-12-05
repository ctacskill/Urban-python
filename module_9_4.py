from random import choice

from bottle import unicode

first = 'Мама мыла раму'
second = 'Рамена мало было'

list_ = list(map(lambda one, two: one == two, first, second))
a = [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
print(a == list_)

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        for data in data_set:
            with open(file_name, 'a', encoding= 'utf-8') as file:
                file.write(str(data))
                file.write('\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    from random import choice
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())