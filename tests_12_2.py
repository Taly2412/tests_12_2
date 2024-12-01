import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results, sep='\n')

    def test_tournament_1(self):
        _tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner3.name)

    def test_tournament_2(self):
        _tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner3.name)

    def test_tournament_3(self):
        _tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner3.name)


if __name__ == "__main__":
    unittest.main()
