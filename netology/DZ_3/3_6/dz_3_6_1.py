from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from engine import engine

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', backref='publisher')


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    stocks = relationship('Stock', backref='book')
    publisher = relationship('Publisher', backref='books')


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer, nullable=False)
    sales = relationship('Sale', backref='stock')
    shop = relationship('Shop', backref='stocks')
    book = relationship('Book', backref='stocks')


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    date_sale = Column(DateTime, nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
    count = Column(Integer, nullable=False)


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db = Session()