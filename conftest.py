import pytest

from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api():
    client = ApiClient()
    yield client
    client.session.close()
