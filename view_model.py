class ViewModel:     
    def __init__(self, items):   
        self._items = items   

    @property
    def items(self):
        return self._items 

    @property
    def todo_items(self):
        todo_filter = [item for item in self._items if item.status == 'To Do']
        return todo_filter

    @property
    def doing_items(self):
        doing_filter = [item for item in self._items if item.status == 'Doing']
        return doing_filter

    @property
    def done_items(self):
        done_filter = [item for item in self._items if item.status == 'Done']
        return done_filter