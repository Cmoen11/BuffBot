import sqlite3


class Database():
    def __init__(self):
        self.conn = None
        print("Opened database successfully")

    def flag_gaming_channel(self, channel_id, game_title, allowed):
        self.conn = sqlite3.connect('test123.db')
        sql = 'insert into game_restriction (channel_ID, title, allowed) ' \
              'VALUES ("{}","{}",{})'.format(channel_id, game_title, allowed)

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def get_flagged_games(self, channel_id):
        flagged_games = []
        self.conn = sqlite3.connect('test123.db')
        games = self.conn.execute("select title from game_restriction where channel_ID = {} and allowed = 1"
                                  .format(channel_id))

        for game in games:
            flagged_games.append(game[0])

        self.conn.close()
        return flagged_games


