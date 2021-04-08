import pytest
import trello as trello
import Item as it
import view_model as view_model
import datetime
    
@pytest.fixture
def test_items():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days= 1)
    item_list = []
    item_list.append(it.Item(1, 'To Do', 'Test1', str(today)))
    item_list.append(it.Item(2, 'To Do', 'Test2', str(today)))
    item_list.append(it.Item(3, 'Doing', 'Test3', str(today)))
    item_list.append(it.Item(4, 'Doing', 'Test4', str(today)))
    item_list.append(it.Item(5, 'Done', 'Test5', str(today)))
    item_list.append(it.Item(6, 'Done', 'Test6', str(today)))
    item_list.append(it.Item(7, 'Done', 'Test6', str(today)))
    item_list.append(it.Item(8, 'Done', 'Test6', str(today)))
    item_list.append(it.Item(9, 'Done', 'Test6', str(today)))
    item_list.append(it.Item(10, 'Done', 'Test6', str(yesterday)))
    item_list.append(it.Item(11, 'Done', 'Test6', str(yesterday)))

    test_list = view_model.ViewModel(item_list)

    return test_list

@pytest.fixture
def test_items2():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days= 1)
    item_list = []
    item_list.append(it.Item(1, 'To Do', 'Test1', str(today)))
    item_list.append(it.Item(2, 'To Do', 'Test2', str(today)))
    item_list.append(it.Item(3, 'Doing', 'Test3', str(today)))
    item_list.append(it.Item(4, 'Doing', 'Test4', str(today)))
    item_list.append(it.Item(5, 'Done', 'Test5', str(today)))
    item_list.append(it.Item(10, 'Done', 'Test6', str(yesterday)))
    item_list.append(it.Item(11, 'Done', 'Test6', str(yesterday)))

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

    assert len(done) == 7

def test_recent_done_items(test_items):
    today_items = test_items.recent_done_items

    assert len(today_items) == 5

def test_older_done_items(test_items):
    today_items = test_items.older_done_items

    assert len(today_items) == 2

def test_show_all_items_more_than_5(test_items):
    show_all = test_items.show_all_done

    assert len(show_all) == 5

def test_show_all_items_less_than_5(test_items2):
    show_all = test_items2.show_all_done

    assert len(show_all) == 3