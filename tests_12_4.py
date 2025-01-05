import unittest
import logging
from logging.config import fileConfig


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers



class TestRunner(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner('sergey', -1)
            for distance in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info(f'test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)



    def test_run(self):
        try:
            runner_1 = Runner(2)
            for distance in range(10):
                runner_1.run()
            self.assertEqual(runner_1.distance, 100)
            logging.info(f'test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для обьекта Runner', exc_info=True)



    def test_challenge(self):
        runner_1 = Runner('sergey')
        runner_2 = Runner('Serega')
        for distance in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format='%(levelname)s | %(massage)s', encoding='UTF-8')

    unittest.main()