import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("A", "B", 1, 2),
            Player("C", "D", 3, 4),
            Player("E", "F", 5, 6),
            Player("G", "H", 7, 8),
            Player("I", "J", 9, 10),
            Player("K", "L", 11, 12),
            Player("M", "N", 13, 14),
            Player("O", "P", 15, 16)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_stats(self):
        self.assertEqual(str(self.stats.search("C")), "C D 3 + 4 = 7")
        self.assertEqual(str(self.stats.search("K")), "K L 11 + 12 = 23")
        self.assertEqual(self.stats.search("Z"), None)
        self.assertEqual(len(self.stats.team("D")), 1)
        self.assertEqual(len(self.stats.team("Q")), 0)
        self.assertEqual(str(self.stats.top(1)[0]), "O P 15 + 16 = 31")
        self.assertEqual(str(self.stats.top(2)[1]), "M N 13 + 14 = 27")
        self.assertEqual(str(self.stats.top(3)[2]), "K L 11 + 12 = 23")
