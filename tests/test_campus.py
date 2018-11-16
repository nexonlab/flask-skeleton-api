def test_post_inscricao(client):
    response = client.get('/campus/')
    assert response is not None
