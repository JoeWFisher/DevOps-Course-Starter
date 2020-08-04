import pytest
import view_model
import trello_items as trello
import datetime
from trello_config import OUTSTANDING, PENDING, DONE
from dateutil.parser import parse

# TODO work out how to mock the today() method tho make the tests have cosistent results


class TestFilters:

    @staticmethod
    def test_outstanding_item_filter():
        # Arrange
        test_items = []
        test_items.append(trello.Item({'id':'1', 'name': 'Item 1', 'due': '2020-07-20 10:35:00 UTC', 'idList': OUTSTANDING, 'desc':'Item 1 description'}))
        test_items.append(trello.Item({'id':'2', 'name': 'Item 2', 'due': '2020-07-20 10:35:00 UTC', 'idList': PENDING, 'desc':'Item 2 description'}))
        test_items.append(trello.Item({'id':'3', 'name': 'Item 3', 'due': '2020-08-04 10:35:00 UTC', 'idList': DONE, 'desc':'Item 3 description'}))
        test_items.append(trello.Item({'id':'4', 'name': 'Item 4', 'due': '2020-07-19 10:35:00 UTC', 'idList': DONE, 'desc':'Item 4 description'}))
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.outstanding_items
        # Assert
        assert any(x.status == 'Not Started' for x in filtered_items)
        assert not any(x.status == 'In Progress' for x in filtered_items)
        assert not any(x.status == 'Completed' for x in filtered_items)
        assert not any(x.status == 'Archived' for x in filtered_items)
    
    @staticmethod
    def test_pending_item_filter():
        # Arrange
        test_items = []
        test_items.append(trello.Item({'id':'1', 'name': 'Item 1', 'due': '2020-07-20 10:35:00 UTC', 'idList': OUTSTANDING, 'desc':'Item 1 description'}))
        test_items.append(trello.Item({'id':'2', 'name': 'Item 2', 'due': '2020-07-20 10:35:00 UTC', 'idList': PENDING, 'desc':'Item 2 description'}))
        test_items.append(trello.Item({'id':'3', 'name': 'Item 3', 'due': '2020-08-04 10:35:00 UTC', 'idList': DONE, 'desc':'Item 3 description'}))
        test_items.append(trello.Item({'id':'4', 'name': 'Item 4', 'due': '2020-07-19 10:35:00 UTC', 'idList': DONE, 'desc':'Item 4 description'}))
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.pending_items
        # Assert
        assert not any(x.status == 'Not Started' for x in filtered_items)
        assert any(x.status == 'In Progress' for x in filtered_items)
        assert not any(x.status == 'Completed' for x in filtered_items)
        assert not any(x.status == 'Archived' for x in filtered_items)

    @staticmethod
    def test_completed_item_filter():
        # Arrange
        test_items = []
        test_items.append(trello.Item({'id':'1', 'name': 'Item 1', 'due': '2020-07-20 10:35:00 UTC', 'idList': OUTSTANDING, 'desc':'Item 1 description'}))
        test_items.append(trello.Item({'id':'2', 'name': 'Item 2', 'due': '2020-07-20 10:35:00 UTC', 'idList': PENDING, 'desc':'Item 2 description'}))
        test_items.append(trello.Item({'id':'3', 'name': 'Item 3', 'due': '2020-08-04 10:35:00 UTC', 'idList': DONE, 'desc':'Item 3 description'}))
        test_items.append(trello.Item({'id':'4', 'name': 'Item 4', 'due': '2020-07-19 10:35:00 UTC', 'idList': DONE, 'desc':'Item 4 description'}))
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.completed_items
        # Assert
        assert not any(x.status == 'Not Started' for x in filtered_items)
        assert not any(x.status == 'In Progress' for x in filtered_items)
        assert any(x.status == 'Completed' for x in filtered_items)
        assert not any(x.status == 'Archived' for x in filtered_items)

    @staticmethod
    def test_archived_item_filter():
        # Arrange
        test_items = []
        test_items.append(trello.Item({'id':'1', 'name': 'Item 1', 'due': '2020-07-20 10:35:00 UTC', 'idList': OUTSTANDING, 'desc':'Item 1 description'}))
        test_items.append(trello.Item({'id':'2', 'name': 'Item 2', 'due': '2020-07-20 10:35:00 UTC', 'idList': PENDING, 'desc':'Item 2 description'}))
        test_items.append(trello.Item({'id':'3', 'name': 'Item 3', 'due': '2020-08-04 10:35:00 UTC', 'idList': DONE, 'desc':'Item 3 description'}))
        test_items.append(trello.Item({'id':'4', 'name': 'Item 4', 'due': '2020-07-19 10:35:00 UTC', 'idList': DONE, 'desc':'Item 4 description'}))
        # Act
        view = view_model.ViewModel(test_items)
        filtered_items = view.archived_items
        # Assert
        assert not any(x.status == 'Not Started' for x in filtered_items)
        assert not any(x.status == 'In Progress' for x in filtered_items)
        assert not any(x.status == 'Completed' for x in filtered_items)
        assert any(x.status == 'Archived' for x in filtered_items)