from sqlalchemy import String, Column
from sqlalchemy.orm import Mapped, mapped_column, scoped_session, sessionmaker
from dataBase import Base, conn

def create_tablename_table(table_name):
    class Parser(Base):
        __tablename__ = table_name

        name: Mapped[str] = mapped_column(primary_key=True)
        price: Mapped[str] = mapped_column(String(50))

        def __init__(self, name, price):

            self.name = name
            self.price = price

    Base.metadata.create_all(conn)
    return Parser

Dbsession = scoped_session(sessionmaker(bind=conn))



