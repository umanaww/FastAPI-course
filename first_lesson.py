from fastapi import FastAPI
from pydantic import EmailStr

app = FastAPI()


@app.get('/hello/')
def hello(name: str):
    name = name.strip().title()
    return 'Hello  ' + name


@app.get('/laguages')
def list_languages():
    return [
        'Russian',
        'English',
        'Polish',
    ]


@app.get('/createuser')
def get_user(name: str, age: int, email: EmailStr):
    if age < 18:
        return 'Вы слишком молоды'
    else:
        return {
            'Name': name,
            'Age': age,
            'Email': 'Accept'
        }
