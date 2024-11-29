from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на вас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} дней, осталось {enemies} врагов')

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

