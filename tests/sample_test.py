import pytest
from blog import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    test_client = app.test_client()
    yield test_client
    test_client.delete()


def test_flask_simple(client):
    result = client.get('/info')
    assert b'About' in result.data
