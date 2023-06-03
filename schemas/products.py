from pydantic import BaseModel,Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int]= None
    name: str= Field(max_length= 50, min_length= 2, description= "Nombre del producto en stock")
    brand: str= Field(max_length= 50, min_length= 2, description= "Nombre de la marca del producto")
    description: str= Field(max_length= 200, min_length= 3, description= "Descripción del producto")
    price: float= Field(len=100)
    entry_date: str= Field(max_length= 10, min_length= 10, description= "Fecha de entrada del producto a stock")
    availability: bool= Field(description= "¿El prducto esta disponible?")
    available_quantity: int= Field(len=10, description= "Cantidad de productos disponibles en stock")

    class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'Leche',
                    'brand': "Alpina",
                    'description':"Bebida de origen animal, blanca, rica en calcio",
                    'price': 2.50,
                    'entry_date':'02/06/2023',
                    'availability': True,
                    'available_quantity': 40
                }
            }