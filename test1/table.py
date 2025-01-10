from dataBase import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import Mapped, mapped_column


class Parser(Base):
    __tablename__ = "parser"

    name: Mapped[str] = mapped_column(primary_key=True)
    price: Mapped[str] = mapped_column(String(50))

    def __init__(self, name, price):

        self.name = name
        self.price = price
