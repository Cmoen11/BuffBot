import sqlite3
import discord

class Database():
    def __init__(self, bot=None):
        self.bot = bot
        self.conn = None
        self.DB_NAME = "test123.db"
        self.wealthTaxPercentage = 0.1
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


    def insert_coins(self, userid, coins, mention=None):
        self.conn = sqlite3.connect(self.DB_NAME)

        if mention == None and self.bot != None: mention = self.bot.Client.get_user_info(userid)

        if mention != None:
            sql = "INSERT OR IGNORE INTO members (userid, coins, user_mention) VALUES(?,0,?);"
            self.conn.execute(sql, (userid, mention,))
            params = (coins, mention, userid,)
            sql = "UPDATE members SET coins = coins + ?, user_mention = ? WHERE userid = ?;"

        elif mention == None:
            sql = "INSERT OR IGNORE INTO members (userid, coins) VALUES(?,0,?);"
            self.conn.execute(sql, (userid,))
            params = (coins, userid,)
            sql = "UPDATE members SET coins = coins + ? WHERE userid = ?;"

        self.conn.execute(sql, params)
        self.conn.commit()
        self.conn.close()

    def remove_coins(self, userid, coins, mention=None):
        self.conn = sqlite3.connect(self.DB_NAME)

        if mention == None and self.bot != None: mention = self.bot.Client.get_user_info(userid)

        if mention != None :
            sql = "INSERT OR IGNORE INTO members (userid, coins, user_mention) VALUES(?,0,?);"
            self.conn.execute(sql, (userid,mention,))
            params = (coins, mention, userid,)
            sql = "UPDATE members SET coins = coins - ?, user_mention = ? WHERE userid = ?;"

        elif mention == None :
            sql = "INSERT OR IGNORE INTO members (userid, coins) VALUES(?,0,?);"
            self.conn.execute(sql, (userid,))
            params = (coins, userid,)
            sql = "UPDATE members SET coins = coins - ? WHERE userid = ?;"


        self.conn.execute(sql, params)
        self.conn.commit()
        self.conn.close()

    def get_coins(self, userid):
        self.conn = sqlite3.connect(self.DB_NAME)
        sql = "INSERT OR IGNORE INTO members (userid, coins) VALUES(?,0);"
        self.conn.execute(sql, (userid,))
        sql = "SELECT coins, userid FROM members WHERE userid = ?"
        params = (userid,)
        result = self.conn.execute(sql, params)
        output = 0
        for i in result :
            output = output + i[0]

        self.conn.close()

        return output

    def get_top_coin_holders(self):
        toplist = []
        self.conn = sqlite3.connect(self.DB_NAME)
        sql = "SELECT userid, coins, user_mention FROM members ORDER BY coins DESC LIMIT 5;"
        result = self.conn.execute(sql)
        for user in result:
            toplist.append({"userid" : user[0], "coins" : user[1], "mention" : user[2]})
        self.conn.close()
        return toplist

    def get_2k_coin_values(self):
        users = []
        self.conn = sqlite3.connect(self.DB_NAME)
        sql = "SELECT userid, coins, user_mention FROM members WHERE MEMBERS.coins >= 2000;"
        result = self.conn.execute(sql)
        for user in result:
            users.append({"userid" : user[0], "coins" : user[1], "mention" : user[2]})
            print(self.get_coins(user[0]))




if __name__ == '__main__':
    db = Database()
    db.get_2k_coin_values()



