from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola mundo!'}


@app.get('/index', response_class=HTMLResponse)
def read_index():
    return """
    <html>
      <head>
        <title>FastAPI do Zero - Alexeiev</title>
      </head>
      <body>
        <h1> olá mundo </h1>
      </body>
    </html>"""
