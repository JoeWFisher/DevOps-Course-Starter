import pytest
import trello as trello
import Item as it
import view_model as view_model
    
@pytest.fixture
def test_items():
    item_list = []
    item_list.append(it.Item(1, 'To Do', 'Test1'))
    item_list.append(it.Item(2, 'To Do', 'Test2'))
    item_list.append(it.Item(3, 'Doing', 'Test3'))
    item_list.append(it.Item(4, 'Doing', 'Test4'))
    item_list.append(it.Item(5, 'Done', 'Test5'))
    item_list.append(it.Item(6, 'Done', 'Test6'))

    test_list = view_model.ViewModel(item_list)

    return test_list

def test_to_do_items(test_items):
    todo = test_items.todo_items

    assert len(todo) == 2

def test_doing_items(test_items):
    doing = test_items.doing_items

    assert len(doing) == 2

def test_done_items(test_items):
    done = test_items.done_items

    assert len(done) == 2
