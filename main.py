from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine,Base
from middlewares.error_handler import Errorhandler


from routers.products import product_router
from routers.supplier import supplier_router


inventory= FastAPI()
inventory.title = "Mi app para un inventario con FastAPI"
inventory.version = "0.0.1"


inventory.add_middleware(Errorhandler)
inventory.include_router(product_router)
inventory.include_router(supplier_router)


Base.metadata.create_all(bind=engine)


@inventory.get ('/')
def root():
    return HTMLResponse ('<h1>Esta es la API de Marianny</h1>')

@inventory.get('/home')
def home():
    return HTMLResponse('<h1>Hello World</h1>')

