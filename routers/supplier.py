from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.supplier import Supplier as ModelSupplier
from schemas.supplier import Supplier as SchemaSupplier
from services.supplier import ServiceSupplier



supplier_router= APIRouter()

@supplier_router.get('/supplier', tags=['Supplier'], status_code=200)
def get_supplier():
    db= Session()
    result= ServiceSupplier(db).get_supplier()
    return JSONResponse(content= jsonable_encoder(result), status_code= 200)

@supplier_router.get ('/supplier/{id}', tags= ['Supplier'], status_code= 202)
def get_supplier_id(id:int):
    db = Session()
    result = ServiceSupplier(db).get_supplier_for_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=202)

@supplier_router.post ('/supplier', tags= ['Supplier'], status_code=201)
def create_supplier(supplier:SchemaSupplier):
    db = Session()
    ServiceSupplier(db).create_supplier(supplier)
    return JSONResponse(content={"message":"Added supplier successfully", "status_code":201})

@supplier_router.put ('/supplier', tags=['Supplier'], status_code=303)
def update_supplier(id:int, data:SchemaSupplier):
    db= Session()
    result= ServiceSupplier(db).get_supplier_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code":404})
    ServiceSupplier(db).update_supplier(id, data)
    return JSONResponse(content={"message":"supplier updated succesfully", "status_code":200}, status_code=200)

@supplier_router.delete('/supplier{id}', tags=['Supplier'])
def delete_supplier(id:int):
    db= Session()
    result= ServiceSupplier(db).get_supplier_for_id(id)
    if not result:
        return JSONResponse(content={"message":"supplier don't found", "status_code":404})
    ServiceSupplier(db).delete_supplier(id)
    return JSONResponse (content={"message": "supplier deleted succesfully", "status_code ":200}, status_code=200 )
