'''
pitfall: inside dir 'templates' run 'pytest'.
pitfall: do not: 'py test_main.py' 
'''


import pytest
from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):  # used to be: test_redirect(client)
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "/"
    '''
    This testcase is redirecting to "/", i.e. to test_index(client) below.
    '''


def test_index(client): # used to be: test_index(client). "index" is less descriptive than "home"
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"<title>About</title>" in response.data


""" Write your own tests below."""















