from models.supplies import Supplies as ModelSupplies
from schemas.supplies import Supplies as SchemaSupplies

class ServiceSupplies():

    def __init__(self, db):
        self.db= db
    
    def get_supplies(self):
        result= self.db.query(ModelSupplies).all()
        return result

    def get_supplies_for_id(self, id:int):
        result = self.db.query(ModelSupplies).filter(ModelSupplies.id == id).first()
        return result

    def create_supplie(self, supplie:ModelSupplies):
        new_supplie = ModelSupplies(
            supplier_id= supplie.supplier_id,
            product_id= supplie.product_id,
            purchase_price= supplie.purchase_price
        )
        self.db.add(new_supplie)
        self.db.commit()
        return

    def update_supplie (self, id:int, data:ModelSupplies):
        supplie = self.db.query(ModelSupplies).filter(ModelSupplies.id == id).first()
        supplie.supplier_id = data.supplier_id
        supplie.product_id = data.product_id
        supplie.purchase_price = data.purchase_price
        self.db.commit()
        return

    def delete_supplie(self, id: int):
        self.db.query(ModelSupplies).filter(ModelSupplies.id == id).delete()
        self.db.commit()
        return
