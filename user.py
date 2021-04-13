from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id):

        self.id = user_id['id']
        self.name = user_id['login']


    @property
    def role(self):
        if self.id == 47788504:
            return 'admin'
        else:
            return 'reader'