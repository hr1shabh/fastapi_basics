from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = ovveride_get_current_user

def test_return_user(test_user):
    response = client.get('/users')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'hrishabh_test'
    assert response.json()['email'] == 'hrishabh@gmail.com'
    assert response.json()['first_name'] == 'Hrishabh'
    assert response.json()['last_name'] == 'Palsra'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '9999999999'
