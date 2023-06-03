from pydantic import BaseModel,Field
from typing import Optional

class Supplier(BaseModel):
    id: Optional[int]= None
    name: str= Field(max_length= 50, min_length= 3, description="Nombre del proveedor")
    address: str= Field(max_length= 50, min_length= 10, description="Dirección del proveedor")
    phone: int= Field(len= 10, description="Teléfono del proveedor")
    email: str= Field(max_length= 50, description="Correo electrónico del proveedor")

    class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'Alpina',
                    'address': "Calle 150 #41-59 Edificio Sumapaz",
                    'phone': 3104867766,
                    'email': "tudistrideconfianza@ventas.com"
                }
            }