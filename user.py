from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id):

        self.id = user_id['id']
        self.name = user_id['login']
        
        try:
            self.role = user_id['role']
        except KeyError:
            self.role = 'reader'
