import unittest
from database import Database
db = Database()


# test flag_gaming channel
# sql  connect  test
# sql insert into test

class DatabaseTest(unittest.TestCase):
    def test_flagged_games(self):
        #Problem: No channels exist in the static db. We would need to run the bot and then get the real channels OR
        # create fake channels
        self.flag_gaming_channel("Jail", "Rocker Leuge", 1)
        self.assertEqual(db.get_flagged_games(), 0)


if __name__ == '__main__':
    unittest.main(exit=False)