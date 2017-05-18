import unittest
import sqlite3
from BuffBot.database import Database


class DatabaseTest(unittest.TestCase):
    # Prepare the relevant table for testing by deleting all rows in it.
    def emptyTable(self, table):
        self.conn = sqlite3.connect("test123.db")
        sql = 'delete from {} '.format(table)
        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    # Querry all the actual data in the relevant testing tables.
    def real_db(self):
        self.conn = sqlite3.connect("test123.db")
        sql = 'select * from game_restriction, members'
        self.conn.execute(sql)
        self.conn.close()
    #Return the querry


    def setUp(self):
        self.actual_db = self.real_db
        self.emptyTable('game_restriction')
        self.emptyTable('members')
        # Create a Database object to call the relevant functions.
        self.db = Database()
        # Insert dummy data into the database.
        self.db.flag_gaming_channel("1", "Hearthstone", 1)
        self.db.insert_coins(85431603408420864, 4000, 'Lenny#1112')
        self.db.insert_coins(235892294857916417, 23, 'Christian#1111')
        self.db.insert_coins(278286021903515656, 20000, 'BuffBot#0334')  # Mocking the bot user.

    def test_flagged_games(self):
        self.assertEqual(self.db.get_flagged_games("1"), ["Hearthstone"])

    def test_get_rich_users(self):
        self.assertEqual([{'userid': 85431603408420864, 'coins': 4000, 'mention': 'Lenny#1112'}], self.db.get_rich_users(278286021903515656, 24))

    def test_poor_users_in_rich_users(self):
        self.assertNotIn([{'userid': 235892294857916417, 'coins': 23, 'mention': 'Christian#1111'}], self.db.get_rich_users(278286021903515656, 24))

    def test_is_bot_in_rich_users(self):
        self.assertNotIn([{'userid': 278286021903515656, 'coins': 20000, 'mention': 'BuffBot#0334'}],
                         self.db.get_rich_users(278286021903515656, 24))

    @classmethod
    def tearDownClass(cls):
        cls.actual_db



if __name__ == '__main__':
    unittest.main(exit=False)