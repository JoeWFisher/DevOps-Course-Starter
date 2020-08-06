from dateutil.parser import parse

class Item:
    def __init__(self, id, title, status, description, editDatetime):
        self.id = id
        self.title = title
        self.status = status
        self.description = description
        self.editDatetime = editDatetime

    @classmethod
    def from_trello_card(cls, card, status):
        return cls(card['id'], card['name'], status, card['desc'], parse(card['dateLastActivity']))

    def set_status_not_started(self):
        self.status = 'Not Started'

    def set_status_in_progress(self):
        self.status = 'In Progress'

    def set_status_completed(self):
        self.status = 'Done'