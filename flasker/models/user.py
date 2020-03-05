from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from .db import Base, session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
    fist_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)

    def __init__(self, user_name, password, first_name, last_name,
                 phone_number, email):
        self.user_name = user_name
        self.password = password
        self.fist_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


    @classmethod
    def get_member(cls, user_name):
        return session.query(cls).filter(
            cls.user_name == user_name
        ).one_or_none()

    @classmethod
    def add_member(cls, user):
        session.add(user)
        session.commit()

    @classmethod
    def get_member_by_id(cls, user_id):
        return session.query(cls).filter(
            cls.id == int(user_id)
        ).one_or_none()

