
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


from .db import Base, session


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    replied_id = Column(Integer, ForeignKey('message.id'))
    sender = relationship(
        'User',
        foreign_keys=[sender_id],
        backref='sent_messages'
    )
    receiver = relationship(
        'User',
        foreign_keys=[receiver_id],
        backref='received_messages'
    )
    reply_to = relationship(
        'Message',
        backref='parent_message',
        uselist=False,
        remote_side=id
    )
    created_at = Column(DateTime)


    def __init__(self, title, body, create_at=None, reply_to=None):
        self.title = title
        self.body = body
        self.created_at = create_at
        self.reply_to = reply_to

