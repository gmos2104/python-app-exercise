from unittest.mock import Mock

from src.Services.ApiService import ApiService


def test_api_service_execution():
    MockedDataFetcher = Mock()
    MockedDataFetcher.fetch_data.return_value = [
        {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False,
        },
    ]
    MockerDataSaver = Mock()

    service = ApiService()
    service.fetcher = MockedDataFetcher
    service.storage = MockerDataSaver

    service.run()

    assert MockedDataFetcher.fetch_data.called
    assert MockerDataSaver.save_data.call_count == 2


def test_api_service_execution_no_data():
    MockedDataFetcher = Mock()
    MockedDataFetcher.fetch_data.return_value = None
    MockerDataSaver = Mock()

    service = ApiService()
    service.fetcher = MockedDataFetcher
    service.storage = MockerDataSaver

    service.run()

    assert MockedDataFetcher.fetch_data.called
    assert not MockerDataSaver.save_data.called
