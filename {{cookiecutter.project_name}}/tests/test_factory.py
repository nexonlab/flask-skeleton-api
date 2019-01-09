# testa se uma aplicacao em modo de teste esta sendo construida
def test_config(app):
    assert app.testing
