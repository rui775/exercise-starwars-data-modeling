from enum import Enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#

class Product(Base):
    __tablename__ = 'product'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    pricing = Column(Float, nullable=False)
    weight = Column(Float)
    color = Column(String(250))

class Costumer(Base):
    __tablename__ = 'costumer'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    address = Column(String(250))

class Bill(Base):
    __tablename__ = 'bill'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)    
    total_price = Column(Float, nullable=False)
    status = Column(Enum("paid","pending","refunded","cancelled"), nullable=False)

class Shopping_Cart(Base):
    __tablename__ = 'shopping_cart'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product")
    costumer_id = Column(Integer, ForeignKey('costumer.id'))
    costumer = relationship("Costumer")
    bill_id = Column(Integer, ForeignKey('bill.id'))
    bill = relationship("Bill")
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    post_code = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
