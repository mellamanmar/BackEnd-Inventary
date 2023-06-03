from sqlalchemy import Column, Integer, Float, String,ForeignKey, Date, Boolean
from config.database import Base
from sqlalchemy.orm import relationship

class Supplier(Base):
    __tablename__="Supplier"

    id= Column (Integer, primary_key=True)
    name= Column (String)
    address= Column (String)
    phone= Column(Integer)
    email= Column(String)

    # supplies = relationship("Supplies", back_populates="Supplier", foreign_keys='Supplies.supplier_id')