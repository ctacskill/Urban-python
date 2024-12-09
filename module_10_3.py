import threading
from threading import Thread
from time import sleep
from random import randint


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        try:
            for _ in range(100):
                money = randint(50, 500)
                self.balance += money
                print(f'Пополнение: {money}. Баланс: {self.balance}')
                sleep(0.001)
                if self.balance >= 500 and self.lock:
                    self.lock.release()
        except RuntimeError:
            pass

    def take(self):
        for _ in range(100):
            money = randint(50, 500)
            print(f'Запрос на {money}')
            if money <= self.balance:
                self.balance -= money
                print(f'Снятие: {money}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен. Недостаточно средств')
                self.lock.acquire()

bk = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bk, ))
thread2 = threading.Thread(target=Bank.take, args=(bk, ))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f'Итоговый баланс: {bk.balance}')