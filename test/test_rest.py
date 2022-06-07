import json
from src.restapi.rest_api import me, index


def test_me_route():
    assert me() == json.dumps({'name': 'Lucas'})

def test_index_route():
    assert index() == json.dumps({'name': 'Alice'})