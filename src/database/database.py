from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
Base = declarative_base()

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

def create_tables():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def store_menu_data(menu_data):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    for data in menu_data:
        # Here you should parse the data to extract menu items and prices
        # For now, we will assume data is a list of dictionaries with 'name' and 'price' keys
        for item in data:
            menu_item = MenuItem(name=item['name'], price=item['price'])
            session.add(menu_item)

    session.commit()
    session.close()
