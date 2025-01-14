from sqlmodel import SQLModel, create_engine

db = create_engine("sqlite:///database.db", echo=True)

def create_db_and_tables():
  SQLModel.metadata.create_all(db)
