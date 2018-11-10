import pytest
import server.main
from flask import url_for
from flask import Flask
import base64

@pytest.yield_fixture(autouse=True)
def run_around_tests():
    file = open('db.json', "w+")
    file.write('[]')

@pytest.fixture
def client():
    server.main.app.testing = True
    client = server.main.app.test_client()
    yield client


def test_ping(client):
    res = client.get('/students')
    assert res.status_code == 200



def test_update(client):
    pass

def test_delete(client):
    pass