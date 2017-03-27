import unittest
import sqlite3
from BuffBot.database import Database


class DatabaseTest(unittest.TestCase):
    # Prepare the relevant table for testing by deleting all rows in it.
    def emptyTable(self, table):
        self.conn = sqlite3.connect(Database.self.DB_NAME)
        sql = 'delete from {} '.format(table)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def setUp(self):
        self.emptyTable("game_restriction")
        # Create a Database object we can call functions on.
        self.db = Database()
        # Insert dummy data into the database.
        self.db.flag_gaming_channel("1", "Hearthstone", 1)

    def test_flagged_games(self):
        self.assertEqual(self.db.get_flagged_games("1"), ["Hearthstone"])


if __name__ == '__main__':
    unittest.main(exit=False)