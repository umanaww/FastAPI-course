from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, APIRouter

router = APIRouter(prefix='/languages', tags=["Languages"])


@router.get('/')
def list_languages():
    languages = ['Russian',
                 'English',
                 'Polish', ]
    return [languages]


@router.get('/{language_id}/')
def get_language_by_id(language_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    languages = ['Russian',
                 'English',
                 'Polish', ]
    if language_id > len(languages) or language_id < 1:
        raise HTTPException(status_code=404, detail='Language not found')
    return {'language': languages[language_id - 1]}
