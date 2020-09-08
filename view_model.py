from config import KEY, TOKEN, BoardID
import requests
import datetime

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
    
    @property
    def recent_done_items(self):
        done_filter = [item for item in self._items if item.status == 'Done']
        today = datetime.date.today()
        recent_list = [item for item in done_filter if item.last_modified.date() == today]
        return recent_list

    @property
    def older_done_items(self):
        done_filter = [item for item in self._items if item.status == 'Done']
        today = datetime.date.today()
        old_list = [item for item in done_filter if item.last_modified.date() < today]
        return old_list

    #I couldn't get this to return ViewModel.done_items ot ViewModel.recent_done_items 
    @property
    def show_all_done(self):
        done_filter = [item for item in self._items if item.status == 'Done']
        if len(done_filter) <= 5:
            return done_filter
        else:
            today = datetime.date.today()
            recent_list = [item for item in done_filter if item.last_modified.date() == today]
            return recent_list

 
