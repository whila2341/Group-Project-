from fastapi.testclient import TestClient
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..controllers import menu_items as controller
from ..main import app
import pytest
from ..models import menu_items as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menu_item(db_session):
    # Create a sample menu item
    item_data = {
        "name": "Turkey Club",
        "description": "Turkey, bacon, lettuce, tomato",
        "ingredients": "turkey, bacon, lettuce, tomato, bread",
        "calories": 550,
        "price": 8.99
    }

    item_object = model.MenuItem(**item_data)

    # Call the create function
    created_item = controller.create(db_session, item_object)

    # Assertions
    assert created_item is not None
    assert created_item.name == "Turkey Club"
    assert created_item.description == "Turkey, bacon, lettuce, tomato"
    assert created_item.ingredients == "turkey, bacon, lettuce, tomato, bread"
    assert created_item.calories == 550
    assert created_item.price == 8.99
    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()


def test_create_menu_item_db_error(db_session, mocker):
    item_data = {
        "name": "Turkey Club",
        "description": "Turkey, bacon, lettuce, tomato",
        "ingredients": "turkey, bacon, lettuce, tomato, bread",
        "calories": 550,
        "price": 8.99
    }
    item_object = model.MenuItem(**item_data)

    error = SQLAlchemyError()
    error.orig = "duplicate entry"
    db_session.commit.side_effect = error

    with pytest.raises(HTTPException) as exc_info:
        controller.create(db_session, item_object)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "duplicate entry"


def test_read_all_menu_items(db_session):
    expected_items = [
        model.MenuItem(id=1, name="Turkey Club", price=8.99),
        model.MenuItem(id=2, name="Veggie Wrap", price=6.50),
    ]
    db_session.query.return_value.all.return_value = expected_items

    result = controller.read_all(db_session)

    assert result == expected_items
    db_session.query.assert_called_once_with(model.MenuItem)


def test_read_all_menu_items_db_error(db_session):
    error = SQLAlchemyError()
    error.orig = "connection lost"
    db_session.query.side_effect = error

    with pytest.raises(HTTPException) as exc_info:
        controller.read_all(db_session)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "connection lost"
