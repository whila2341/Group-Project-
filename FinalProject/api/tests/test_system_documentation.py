from ..controllers import system_documentation as controller
import pytest
from ..models import System_doc as model


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_system_documentation(db_session):
    data = {
        "title": "Employee Manual",
        "category": "Training",
        "content": "Instructions for new employees."
    }

    documentation = model.SystemDocumentation(**data)

    created_documentation = controller.create(db_session, documentation)

    assert created_documentation is not None
    assert created_documentation.title == "Employee Manual"
    assert created_documentation.category == "Training"
    assert created_documentation.content == "Instructions for new employees."