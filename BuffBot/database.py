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
        self.conn = sqlite3.connect(self.DB_NAME)
        games = self.conn.execute("select title from game_restriction where channel_ID = '{}' and allowed = 1"
                                  .format(channel_id))

        for game in games:
            flagged_games.append(game[0])

        self.conn.commit()
        self.conn.close()
        return flagged_games

    def remove_flagged_games(self, channel_id):
        self.conn = sqlite3.connect(self.DB_NAME)
        self.conn.execute("delete from game_restriction WHERE channel_id = '{}';".format(channel_id))
        self.conn.close()

    def get_game_channel(self, title):
        channels = []
        self.conn = sqlite3.connect(self.DB_NAME)
        games = self.conn.execute("select channel_ID from game_restriction where title = '{}' and allowed = 1"
                                  .format(title))

        for game in games:
            channels.append(game[0])

        self.conn.commit()
        self.conn.close()
        return channels

    def set_coin_count_session_start(self, user_id, start_time, end_time, session_active):
        self.conn = sqlite3.connect(self.DB_NAME)
        params = (user_id, start_time, end_time, session_active)
        sql = "INSERT INTO coins VALUES (?, ?, ?, ?)"

        self.conn.execute(sql, params)
        self.conn.commit()
        self.conn.close()

    def set_coin_count_session_end(self, user_id, end_time, session_active):
        self.conn = sqlite3.connect(self.DB_NAME)
        params = (end_time, session_active, user_id)
        sql = "UPDATE coins SET end_time = ?, session_active = ?" \
              "WHERE user_id = ? AND start_time = (SELECT MAX(start_time)  FROM coins);"
        self.conn.execute(sql, params)
        self.conn.commit()
        self.conn.close()

    def get_coin_count(self, user_id):
        # TODO: Implement total coin value in DB as separate row
        self.conn = sqlite3.connect(self.DB_NAME)
        params = (user_id, 0)
        sql = "SELECT start_time, end_time FROM coins WHERE user_id =? and session_active = ?"

        sessions = self.conn.execute(sql, params)

        def format_2_dec(val):
            return "{:.2f}".format(val)

        total_coins = 0
        for session in sessions:
            # Gives 0.5 points for every minute
            total_coins += (session[1] - session[0]) / 60 % 60 * 0.5

        self.conn.close()
        return format_2_dec(total_coins)

