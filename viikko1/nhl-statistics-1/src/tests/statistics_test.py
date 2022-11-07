import unittest
from statistics import Statistics
from player import Player
from statistics import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):

        self.statistics = Statistics(PlayerReaderStub())

    def test_search_works_as_intended(self):
        example = self.statistics.search("Kurri")
        empty = self.statistics.search("abc")

        self.assertAlmostEqual(example.name,"Kurri")
        self.assertAlmostEqual(None,empty)

    def test_team_works_as_intended(self):

        empty = self.statistics.team("abc")
        self.assertEqual(empty,[])
        
        team = self.statistics.team("EDM")
        names = [player.name for player in team]
        self.assertEqual(names,["Semenko","Kurri","Gretzky"])

    def test_top_works_as_intended(self):
        empty = self.statistics.top(-3,SortBy.POINTS)
        self.assertEqual(empty,[])



        top3_by_points = self.statistics.top(2,SortBy.POINTS)
        names1 = [player.name for player in top3_by_points]
        self.assertEqual(names1,["Gretzky","Lemieux","Yzerman"])

        top3_by_goals = self.statistics.top(2,SortBy.GOALS)
        names2 = [player.name for player in top3_by_goals]
        self.assertEqual(names2,["Lemieux","Yzerman","Kurri"])

        top3_by_assists = self.statistics.top(2,SortBy.ASSISTS)
        names3 = [player.name for player in top3_by_assists]
        self.assertEqual(names3,["Gretzky","Yzerman","Lemieux"])

