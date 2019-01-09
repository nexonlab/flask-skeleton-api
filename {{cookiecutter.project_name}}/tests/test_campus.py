# testa se get_campus esta sendo executado
def test_get_campus(client):
    response = client.get('/{{cookiecutter.app_name}}/campus/')
    assert response is not None
