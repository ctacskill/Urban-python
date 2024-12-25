import unittest
from module_12_2 import *
import pprint


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = None

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        d = cls.all_results
        pprint.pprint(d, width=1)

    def test_tournament(self):
        self.all_results = Tournament(90, self.runner_1, self.runner_3).start()
        last = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last, 'Ник')

    def test_tournament_1(cls):
        cls.all_results = Tournament(90, cls.runner_2, cls.runner_3).start()
        last = cls.all_results[max(cls.all_results.keys())]
        cls.assertTrue(last, 'Ник')

    def test_tournament_3(cls):
        cls.all_results = Tournament(90, cls.runner_2, cls.runner_1, cls.runner_3).start()
        last = cls.all_results[max(cls.all_results.keys())]
        cls.assertTrue(last, 'Ник')