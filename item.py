
class Item:

    def __init__(self, id, title, status = 'ToDo'):
        self.id = id
        self.title = title
        self.status = status

    def can_delete(self):
        return self.status == 'Done'

    def next_status(self):
        if self.status == 'ToDo':
            return 'InProgress'
        elif self.status == 'InProgress':
            return 'Done'
        elif self.status == 'Done':
            return 'ToDo'