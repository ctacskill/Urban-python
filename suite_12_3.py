import unittest
import module_12_1
import tests_12_2

runnerTestST = unittest.TestSuite()
runnerTestST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.TestRunner))
runnerTestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)


runner.run(runnerTestST)

