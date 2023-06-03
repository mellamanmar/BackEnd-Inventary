from models.products import Product as ModelProduct
from schemas.products import Product as SchemaProduct

class ServiceProduct ():

    def __init__(self, db):
        self.db= db
    
    def get_product(self):
        result= self.db.query(ModelProduct).all()
        return result

    def get_product_for_id(self,id:int):
        result = self.db.query(ModelProduct).filter(ModelProduct.id == id).first()
        return result

    def create_product(self, product:ModelProduct):
        new_product = ModelProduct( 
            name= product.name,
            brand = product.brand,
            description = product.description,
            price = product.price,
            entry_date = product.entry_date,
            availability = product.availability,
            available_quantity = product.available_quantity 
        )
        self.db.add(new_product)
        self.db.commit()
        return 
    
    def update_product (self, id:int, data:ModelProduct):
        product = self.db.query(ModelProduct).filter(ModelProduct.id == id).first()
        product.name = data.name
        product.brand = data.brand
        product.description = data.description
        product.price = data.price
        product.entry_date = data.entry_date
        product.availability = data.availability
        product.available_quantity = data.available_quantity
        self.db.commit()
        return

    def delete_product(self, id: int):
        self.db.query(ModelProduct).filter(ModelProduct.id == id).delete()
        self.db.commit()
        return