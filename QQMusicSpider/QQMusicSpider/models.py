from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+mysqldb://root:123456@localhost/test?charset=utf8')
Base = declarative_base()


class Singer(Base):
    __tablename__ = 'singers'

    singer_id = Column(Integer, primary_key=True)
    singer_mid = Column(String(256))
    singer_name = Column(String(256), index=True)
    singer_pic = Column(String(256))
    country = Column(String(256))


def create_table():
    Base.metadata.create_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    create_table()
