from ..controllers import data_analysis as controller
import pytest
from ..models import data_analysis as model


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_data_analysis(db_session):
    data = {
        "report_name": "Weekly Sales",
        "metric": "Revenue",
        "value": 1500.75
    }

    analysis = model.DataAnalysis(**data)

    created_analysis = controller.create(db_session, analysis)

    assert created_analysis is not None
    assert created_analysis.report_name == "Weekly Sales"
    assert created_analysis.metric == "Revenue"
    assert created_analysis.value == 1500.75