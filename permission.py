

class Permission():
    def __init__(self):
        self.users = []
        self.permissions = []

    def add_user(self, nickname, userid, permissionID):
        self.users.append({
            'nickname' : nickname,
            'userid' : userid,
            'permissionID' : permissionID
        })