from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy import Engine


class Database:
    def __init__(self):
        connect_args = {"check_same_thread": False}
        self._engine = create_engine("sqlite:///database.db", connect_args=connect_args)

    @property
    def engine(self) -> Engine:
        return self._engine

    def get_session(self):
        with Session(self.engine) as session:
            yield session

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)
