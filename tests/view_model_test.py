import pytest
import view_model
import trello_items as trello
from dotenv import find_dotenv, load_dotenv 
import app
import datetime
from dateutil.parser import parse
from unittest import mock

@pytest.fixture
def test_items():
    test_items = []
    test_items.append(trello.Item.from_trello_card({'id': '1',  'name': 'Item 1',  'desc': 'Item 1 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'Not Started'))
    test_items.append(trello.Item.from_trello_card({'id': '2',  'name': 'Item 2',  'desc': 'Item 2 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'Not Started'))
    test_items.append(trello.Item.from_trello_card({'id': '3',  'name': 'Item 3',  'desc': 'Item 3 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'Not Started'))
    test_items.append(trello.Item.from_trello_card({'id': '4',  'name': 'Item 4',  'desc': 'Item 4 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'Not Started'))
    test_items.append(trello.Item.from_trello_card({'id': '5',  'name': 'Item 5',  'desc': 'Item 5 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'In Progress'))
    test_items.append(trello.Item.from_trello_card({'id': '6',  'name': 'Item 6',  'desc': 'Item 6 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'In Progress'))
    test_items.append(trello.Item.from_trello_card({'id': '7',  'name': 'Item 7',  'desc': 'Item 7 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'In Progress'))
    test_items.append(trello.Item.from_trello_card({'id': '8',  'name': 'Item 8',  'desc': 'Item 8 description',  'dateLastActivity': '2020-08-04 10:35:00 UTC'}, 'In Progress'))
    test_items.append(trello.Item.from_trello_card({'id': '9',  'name': 'Item 9',  'desc': 'Item 9 description',  'dateLastActivity': '2020-08-07 10:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '10', 'name': 'Item 10', 'desc': 'Item 10 description', 'dateLastActivity': '2020-08-07 10:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '11', 'name': 'Item 11', 'desc': 'Item 11 description', 'dateLastActivity': '2020-08-07 10:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '12', 'name': 'Item 12', 'desc': 'Item 12 description', 'dateLastActivity': '2020-08-07 10:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '13', 'name': 'Item 13', 'desc': 'Item 13 description', 'dateLastActivity': '2020-08-03 10:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '14', 'name': 'Item 14', 'desc': 'Item 14 description', 'dateLastActivity': '2020-08-03 10:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '15', 'name': 'Item 15', 'desc': 'Item 15 description', 'dateLastActivity': '2020-08-03 11:35:00 UTC'}, 'Done'))
    test_items.append(trello.Item.from_trello_card({'id': '16', 'name': 'Item 16', 'desc': 'Item 16 description', 'dateLastActivity': '2020-08-03 11:35:00 UTC'}, 'Done'))
    return test_items

class TestFilters:

    @staticmethod
    def test_outstanding_item_filter(test_items):
        # Arrange
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.outstanding_items
        # Assert
        assert any(x.status == 'Not Started' for x in filtered_items)
        assert not any(x.status == 'In Progress' for x in filtered_items)
        assert not any(x.status == 'Done' for x in filtered_items)
    
    @staticmethod
    def test_pending_item_filter(test_items):
        # Arrange
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.pending_items
        # Assert
        assert not any(x.status == 'Not Started' for x in filtered_items)
        assert any(x.status == 'In Progress' for x in filtered_items)
        assert not any(x.status == 'Done' for x in filtered_items)

    @staticmethod
    def test_show_all_done_items(test_items):
        # Arrange
        
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.all_done_items
        # Assert
        assert any(x.id == '9' for x in filtered_items)
        assert any(x.id == '10' for x in filtered_items)
        assert any(x.id == '11' for x in filtered_items)
        assert any(x.id == '12' for x in filtered_items)
        assert any(x.id == '13' for x in filtered_items)
        assert any(x.id == '14' for x in filtered_items)
        assert any(x.id == '15' for x in filtered_items)
        assert any(x.id == '16' for x in filtered_items)

    @staticmethod
    def test_recent_done_items(test_items, monkeypatch):
        target = datetime.date(2020, 8, 7)
        with mock.patch.object(datetime, 'date', mock.Mock(wraps=datetime.date)) as patched:
            patched.today.return_value = target
            # Act
            view = view_model.ViewModel(test_items)
            filtered_items = view.recent_done_items
            # Assert
            assert any(x.id == '9' for x in filtered_items)
            assert any(x.id == '10' for x in filtered_items)
            assert any(x.id == '11' for x in filtered_items)
            assert any(x.id == '12' for x in filtered_items)
            assert not any(x.id == '13' for x in filtered_items)
            assert not any(x.id == '14' for x in filtered_items)
            assert not any(x.id == '15' for x in filtered_items)
            assert not any(x.id == '16' for x in filtered_items)

    @staticmethod
    def test_older_done_items(test_items):
        target = datetime.date(2020, 8, 7)
        with mock.patch.object(datetime, 'date', mock.Mock(wraps=datetime.date)) as patched:
            patched.today.return_value = target
            # Act
            view = view_model.ViewModel(test_items)
            filtered_items = view.older_done_items
            # Assert
            assert not any(x.id == '9' for x in filtered_items)
            assert not any(x.id == '10' for x in filtered_items)
            assert not any(x.id == '11' for x in filtered_items)
            assert not any(x.id == '12' for x in filtered_items)
            assert any(x.id == '13' for x in filtered_items)
            assert any(x.id == '14' for x in filtered_items)
            assert any(x.id == '15' for x in filtered_items)
            assert any(x.id == '16' for x in filtered_items)