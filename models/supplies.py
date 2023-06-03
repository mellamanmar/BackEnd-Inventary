from sqlalchemy import Column, Integer, Float, String,ForeignKey, Date, Boolean
from config.database import Base
from sqlalchemy.orm import relationship


class Supplies(Base):
    __tablename__= "Supplies"

    id= Column(Integer, primary_key=True)
    supplier_id= Column(Integer, ForeignKey("Supplier.id"))
    product_id= Column (Integer, ForeignKey("Product.id"))
    purchase_price= Column(Float)

    # supplier = relationship("Supplier", back_populates="Supplies")
    # product = relationship("Product", back_populates="Supplies")
