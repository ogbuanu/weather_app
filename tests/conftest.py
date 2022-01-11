import pytest
from weather_app import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'API_KEY': '2b274f88a1c8487eb74162859210908'
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()