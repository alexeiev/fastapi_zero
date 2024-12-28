from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root_deve_return_Ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alex',
            'email': 'alex@email.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alex',
        'email': 'alex@email.com',
    }


def test_create_user_with_email_exist_400(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'blablabla',
            'email': 'alex@email.com',
            'password': 'password',
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_with_username_exist_400(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'alex',
            'email': 'blablabla@email.com',
            'password': 'password',
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user_id(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alex',
        'email': 'alex@email.com',
    }


def test_read_user_id_not_exist_return_404(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'alexeiev',
            'email': 'alex@email.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alexeiev',
        'email': 'alex@email.com',
    }


def test_update_user_put_return_404(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'novo',
            'email': 'alex@email.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_deve_retornar_404(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_index_deve_retornar_HTML(client):
    response = client.get('/index')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title>FastAPI do Zero - Alexeiev</title>
      </head>
      <body>
        <h1> olá mundo </h1>
      </body>
    </html>"""
    )
