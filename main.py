from fastapi import FastAPI
from fastapi.responses import HTMLResponse


inventory= FastAPI()
inventory.title = "Mi app con FastAPI"
inventory.version = "0.0.1"


app.add_middleware(Errorhandler)



Base.metadata.create_all(bind=engine)


@inventory.get ('/')
def root():
    return HTMLResponse ('<h1>Esta es la API de Marianny</h1>')

@inventory.get('/home')
def home():
    return HTMLResponse('<h1>Hello World</h1>')

