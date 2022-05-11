from unittest.mock import Mock

from src.Services.ApiService import ApiService


def test_api_service_execution():
    mocked_fetch_data = Mock()
    mocked_fetch_data.return_value = [
        {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False,
        },
    ]
    mocked_save_data = Mock()

    service = ApiService()
    service._fetch_data = mocked_fetch_data
    service._save_data = mocked_save_data

    service.run()

    assert mocked_fetch_data.called
    assert mocked_save_data.call_count == 2


def test_api_service_execution_no_data():
    mocked_fetch_data = Mock()
    mocked_fetch_data.return_value = None
    mocked_save_data = Mock()

    service = ApiService()
    service._fetch_data = mocked_fetch_data
    service._save_data = mocked_save_data

    service.run()

    assert mocked_fetch_data.called
    assert not mocked_save_data.called
