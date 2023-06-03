from sqlalchemy import Column, Integer, Float, String,ForeignKey, Date, Boolean
from config.database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ ="Product"

    id = Column(Integer, primary_key= True)
    name= Column(String)
    brand= Column(String)
    description= Column(String)
    price= Column(Float)
    entry_date= Column(String)
    availability= Column(Boolean)
    available_quantity= Column(Integer)

    # supplies = relationship("Supplies", back_populates="Product", foreign_keys='Supplies.product_id')