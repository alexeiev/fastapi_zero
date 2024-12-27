from http import HTTPStatus


def test_read_root_deve_retornar_Ola_mundo(client):
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alex',
                'email': 'alex@email.com',
            }
        ]
    }


def test_read_user_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alex',
        'email': 'alex@email.com',
    }


def test_read_user_id_deve_retornar_404(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
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


def test_update_user_deve_retornar_404(client):
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


def test_delete_user(client):
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
