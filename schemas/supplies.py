from pydantic import BaseModel,Field
from typing import Optional

class Supplies(BaseModel):
    id: Optional[int]=None
    supplier_id: int= Field(ge=1, description= "Llave foránea del proveedor")
    product_id: int= Field (ge=1, description= "Llave foránea del producto")
    purchase_price: float= Field(len=5, description= "Precio de compra del producto")

    class Config:
        schema_extra= {
            "example":{
                'id':1,
                'supplier_id': 1,
                'product_id': 2,
                'purchase_price': 10
            }
        }