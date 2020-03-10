
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


from .database import db


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)
    body = db.Column(String)
    sender_id = db.Column(Integer, ForeignKey('members.id'))
    receiver_id = db.Column(Integer, ForeignKey('members.id'))
    replied_id = db.Column(Integer, ForeignKey('message.id'))
    sender = relationship(
        'Member',
        foreign_keys=[sender_id],
        backref='sent_messages'
    )
    receiver = relationship(
        'Member',
        foreign_keys=[receiver_id],
        backref='received_messages'
    )
    reply_to = relationship(
        'Message',
        backref='parent_message',
        uselist=False,
        remote_side=id
    )
    created_at = db.Column(DateTime)

    def __init__(self, title, body, create_at=None, reply_to=None):
        self.title = title
        self.body = body
        self.created_at = create_at
        self.reply_to = reply_to

