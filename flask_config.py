import os

class Config:
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY', 'default_key')
        self.LOGIN_DISABLED = os.environ.get('LOAD_DISABLED', 'False')