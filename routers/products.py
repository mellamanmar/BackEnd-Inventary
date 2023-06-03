from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.products import Product as ModelProduct
from services.products import ServiceProduct
from schemas.products import Product as SchemaProduct



product_router= APIRouter()


@product_router.get('/product', tags=['product'], status_code=200)
def get_product():
    db= Session()
    result= ServiceProduct(db).get_product()
    return JSONResponse(content= jsonable_encoder(result), status_code= 200)

@product_router.get ('/product/{id}', tags= ['product'], status_code= 202)
def get_product_id(id:int):
    db = Session()
    result = ServiceProduct(db).get_product_for_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=202)

@product_router.post ('/product', tags= ['product'], status_code=201,response_model=dict)
def create_product(product:SchemaProduct):
    db = Session()
    ServiceProduct(db).create_product(product)
    return JSONResponse(content={"message":"Added product successfully", "status_code":201})

@product_router.put ('/product', tags=['product'], status_code=303)
def update_product(id:int, data:SchemaProduct):
    db= Session()
    result= ServiceProduct(db).get_product_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"product don't found", "status_code":404})
    ServiceProduct(db).update_product(id, data)
    return JSONResponse(content={"message":"product updated succesfully", "status_code":200}, status_code=200)

@product_router.delete('/product{id}', tags=['product'])
def delete_product(id:int):
    db= Session()
    result= ServiceProduct(db).get_product_for_id(id)
    if not result:
        return JSONResponse(content={"message":"product don't found", "status_code":404})
    ServiceProduct(db).delete_product(id)
    return JSONResponse (content={"message": "product deleted succesfully", "status_code ":200}, status_code=200 )
