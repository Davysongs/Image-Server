from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///menus.db") 
Base = declarative_base()

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

def create_database():
    # Check if the database file exists, if not, create it
    db_file = DATABASE_URL.split("///")[-1]
    if not os.path.exists(db_file):
        print("Database not found. Creating a new database.")
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
    else:
        print("Database already exists.")

def store_menu_data(menu_data):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in menu_data:
        menu_item = MenuItem(name=item['name'], price=item['price'])
        session.add(menu_item)

    session.commit()
    session.close()

if __name__ == "__main__":
    create_database()
