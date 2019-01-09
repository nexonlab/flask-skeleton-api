import pytest

from app import create_app
from app.config import TesteConfig


@pytest.fixture
def app():

    app = create_app()
    app.config.from_object(TesteConfig)

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
