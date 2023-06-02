from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app= FastAPI()


@app.get ('/')
def root():
    return HTMLResponse ('<h1>Esta es la API de Marianny</h1>')

@app.get('/home')
def home():
    return HTMLResponse('<h1>Hello World</h1>')