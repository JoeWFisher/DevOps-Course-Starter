import datetime

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def outstanding_items(self):
        return [item for item in self._items if item.status == 'Not Started']
    
    @property
    def pending_items(self):
        return [item for item in self._items if item.status == 'In Progress']

    @property
    def completed_items(self):
        return [item for item in self._items if item.status == 'Completed']

    @property
    def archived_items(self):
        return [item for item in self._items if item.status == 'Archived']