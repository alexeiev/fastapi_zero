from http import HTTPStatus


def test_read_root_deve_return_Ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola mundo!'}


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
