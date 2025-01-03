
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200



def test_index_post(app, client):
    res = client.post('/')
    assert res.status_code == 405
