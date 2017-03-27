import sqlite3


class Database():
    def __init__(self):
        self.conn = None
        self.DB_NAME = "test123.db"
        print("Opened database successfully")

    def flag_gaming_channel(self, channel_id, game_title, allowed):
        self.conn = sqlite3.connect(self.DB_NAME)
        sql = 'insert into game_restriction (channel_ID, title, allowed) ' \
              'VALUES ("{}","{}",{})'.format(channel_id, game_title, allowed)

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def get_flagged_games(self, channel_id):
        flagged_games = []
        self.conn = sqlite3.connect(self.databaseName)
        games = self.conn.execute("select title from game_restriction where channel_ID = {} and allowed = 1"
                                  .format(channel_id))

        for game in games:
            flagged_games.append(game[0])

        self.conn.close()
        return flagged_games

    @classmethod
    def set_coin_count_session_start(self, user_id, start_time, end_time, session_active):
        self.conn = sqlite3.connect(self.DB_NAME)
        sql = 'insert into coins (user_id, start_time, end_time, session_active) ' \
              'VALUES ("{}",{},{})'.format(user_id, start_time, end_time, session_active)

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    @classmethod
    def set_coin_count_session_end(self, user_id, end_time, session_active):
        self.conn = sqlite3.connect(self.DB_NAME)
        sql = 'UPDATE coins SET (end_time = {}, session_active = {}) ' \
              'WHERE user_id = "{}"'.format(end_time, session_active, user_id)

        self.conn.execute(sql)
        self.conn.commit()
        self.conn.close()

    def get_coin_count(self, user_id):
        # TODO: Implement total coin value in DB as separate row
        total_coins = 0
        self.conn = sqlite3.connect(self.DB_NAME)
        sessions = self.conn.execute("select start_time, end_time from coins where user_id = {} and session_active = 0"
                                  .format(user_id))

        for session in sessions:
            # Gives 0.5 points for every minute also
            total_coins += (session.start_time - session.end_time) / 60 * 0.5

        self.conn.close()
        return total_coins


