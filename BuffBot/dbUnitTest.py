import unittest
import sqlite3
from BuffBot.database import Database


class DatabaseTest(unittest.TestCase):
    # Prepare the relevant table for testing by deleting all rows in it.
    def emptyTable(self, table):
        self.conn = sqlite3.connect('test123.db')
        sql = 'delete from {} '.format(table)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def setUp(self):
        self.emptyTable("game_restriction")
        self.emptyTable("main.members")
        # Create a Database object to call the relevant functions.
        self.db = Database()
        # Insert dummy data into the database.
        self.db.flag_gaming_channel("1", "Hearthstone", 1)
        self.db.insert_coins(85431603408420864, 4000, mention=None)
        self.db.insert_coins(235892294857916417, 23, mention=None)
        self.db.insert_coins(278286021903515656, 20000, mention=None)  # Mocking the bot user.

    def test_flagged_games(self):
        self.assertEqual(self.db.get_flagged_games("1"), ["Hearthstone"])

    def test_get_rich_users(self):
        self.assertEqual(self.db.get_rich_users(278286021903515656, 24), 0)


if __name__ == '__main__':
    unittest.main(exit=False)