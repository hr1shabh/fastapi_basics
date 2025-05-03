from http.client import responses

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

def test_change_password_success(test_user):
    response = client.put('/users/change_password', json={'password': 'Test123', 'new_password': 'Test1234'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put('/users/change_password', json={'password': 'wrong', 'new_password': 'Test1234'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Authentication failed'}

def test_change_password_invalid_current_password(test_user):
    response = client.put('/users/change_password', json={'password': 'wrong', 'new_password': 'Test1234'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number_success(test_user):
    response = client.put('users/update_phone_number/989999999')
    assert response.status_code == status.HTTP_204_NO_CONTENT
