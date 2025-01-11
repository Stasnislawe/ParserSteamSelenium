import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import declarative_base
import sqlalchemy


class connects():
    def __init__(self, user, password, db, host="localhost", port=5432):
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self.port = port

    def connectmethod(self):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(self.user, self.password, self.host, self.port, self.db)

        con = sqlalchemy.create_engine(url, client_encoding="utf-8")

        return con


load_dotenv(find_dotenv())
user = os.getenv('USER')
password = os.getenv('PASSWORD')
db = os.getenv('DB')

conn = connects(user, password, db).connectmethod()
Base = declarative_base()