from fastapi import FastAPI
from pydantic import EmailStr, BaseModel, Field
from languages import router as languages_router
from findby.views import router as findby_router

app = FastAPI()
app.include_router(languages_router)
app.include_router(findby_router)


@app.get('/hello/')
def hello(name: str):
    name = name.strip().title()
    return 'Hello  ' + name


languages = ['Russian',
             'English',
             'Polish', ]
