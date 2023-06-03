from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.supplies import Supplies as ModelSupplies
from schemas.supplies import Supplies as SchemaSupplies
from services.supplies import ServiceSupplies

supplies_router= APIRouter()

@supplies_router.get('/supplies',tags=['Supplies'],status_code=200)
def get_supplies():
    db = Session()
    result = ServiceSupplies(db).get_supplies()
    return JSONResponse (content=jsonable_encoder(result),status_code=200)

@supplies_router.get('/supplies{id}',tags=['Supplies'],status_code=200)
def get_supplies_for_id(id:int):
    db = Session()
    result = ServiceSupplies(db).get_supplies_for_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=202)

@supplies_router.post ('/supplies', tags= ['Supplies'], status_code=201,response_model=dict)
def create_supplie(supplie:SchemaSupplies):
    db = Session()
    ServiceSupplies(db).create_supplie(supplie)
    return JSONResponse(content={"message":"Added supplie successfully", "status_code":201})

@supplies_router.put ('/supplies', tags=['Supplies'], status_code=303)
def update_supplie(id:int, data:SchemaSupplies):
    db= Session()
    result= ServiceSupplies(db).get_supplies_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"supplie don't found", "status_code":404})
    ServiceSupplies(db).update_supplie(id, data)
    return JSONResponse(content={"message":"supplie updated succesfully", "status_code":200}, status_code=200)

@supplies_router.delete('/supplies{id}', tags=['Supplies'])
def delete_supplie(id:int):
    db= Session()
    result= ServiceSupplies(db).get_supplies_for_id(id)
    if not result:
        return JSONResponse(content={"message":"supplie don't found", "status_code":404})
    ServiceSupplies(db).delete_supplie(id)
    return JSONResponse (content={"message": "supplie deleted succesfully", "status_code ":200}, status_code=200 )

