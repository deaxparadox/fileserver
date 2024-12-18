import requests

def test_current_user():
    url: str = "http://localhost:9000/v1/users/me"
    res = requests.get(url=url)
    assert res.status_code == 200