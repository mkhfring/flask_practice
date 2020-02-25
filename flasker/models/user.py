from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from .db import Base, session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
    posts = relationship("Post")

    @classmethod
    def get_member(cls, user_name):
        return session.query(cls).filter(
            cls.user_name == user_name
        ).one_or_none()

    @classmethod
    def add_member(cls, user_name, password):
        user = cls(user_name=user_name, password=password)
        session.add(user)
        session.commit()

    @classmethod
    def get_member_by_id(cls, user_id):
        return session.query(cls).filter(
            cls.id == int(user_id)
        ).one_or_none()
