import pytest
import os

from app import create_app
from app.config import TesteConfig


@pytest.fixture
def app():

    settings_override = {
        'SQLALCHEMY_DATABASE_URI': "sqlite:///%steste.db" % os.path.join(os.getcwd(), "instance/"),
        'TESTING': True,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    app = create_app()
    app.config.from_object(TesteConfig)

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
