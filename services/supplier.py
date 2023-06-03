from models.supplier import Supplier as ModelSupplier
from schemas.supplier import Supplier as SchemaSupplier

class ServiceSupplier ():

    def __init__(self, db):
        self.db= db
    
    def get_supplier(self):
        result= self.db.query(ModelSupplier).all()
        return result
    
    def get_supplier_for_id(self,id:int):
        result = self.db.query(ModelSupplier).filter(ModelSupplier.id == id).first()
        return result
    
    def create_supplier(self, supplier:SchemaSupplier):
        new_supplier = ModelSupplier( 
            name= supplier.name,
            address = supplier.address,
            phone = supplier.phone,
            email = supplier.email
        )
        self.db.add(new_supplier)
        self.db.commit()
        return 

    def update_supplier (self, id:int, data:ModelSupplier):
        supplier = self.db.query(ModelSupplier).filter(ModelSupplier.id == id).first()
        supplier.name= data.name
        supplier.address= data.address
        supplier.phone= data.phone
        supplier.email= data.email
        
        self.db.commit()
        return

    def delete_supplier(self, id: int):
        self.db.query(ModelSupplier).filter(ModelSupplier.id == id).delete()
        self.db.commit()
        return