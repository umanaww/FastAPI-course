from fastapi import APIRouter
from .schemas import User
from .crud import users

router = APIRouter(tags=['Find User'])


@router.post('/createuser')
def get_user(user: User):
    if user.age < 18 or user.age is None:
        return 'Вы слишком молоды'
    else:
        users.append(user)
        return {
            'Name': user.name,
            'Age': user.age,
            'Email': 'Accept',
            'Password': '*' * len(user.password)
        }


@router.get('/findby/name/{name}')
def find_by_name(name:str):
    for user in users:
        if user.name == name:
            return user
        else:
            return 'Пользователь не найден'

@router.get('/findby/email/{email}')
def find_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    return 'Пользователь не найден'