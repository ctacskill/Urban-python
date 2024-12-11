from threading import Thread
from queue import Queue
from time import sleep
from random import randint

from pyparsing import White


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        guests = list(guests)
        for i in range(len(self.tables)):
            self.tables[i].guest = guests[i]
            guests[i].start()
            print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')

        for i in range(len(self.tables), len(guests)):
            self.queue.put(guests[i])
            print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        busy = [True for table in self.tables if table.guest is not None]
        while not self.queue.empty() or busy != []:
            for table_ready in self.tables:
                if table_ready.guest is not None:
                    if table_ready.guest.is_alive() is False:
                        print(f'{table_ready.guest.name} покушал(-а) и ушел(-а)')
                        print(f'Стол номер {table_ready.number} освободился')
                        table_ready.guest = None

                if not self.queue.empty():
                    busy_1 = [True for table in self.tables if table.guest is None]
                    if busy_1 != []:
                        table_ready.guest = self.queue.get()
                        print(f'{table_ready.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table_ready.number}')
                        table_ready.guest.start()



tables = [Table(number) for number in range(1, 6)]

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()




