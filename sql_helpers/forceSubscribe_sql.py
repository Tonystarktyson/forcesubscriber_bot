from sqlalchemy import Column, String, BigInteger
from sqlalchemy.exc import SQLAlchemyError
from sql_helpers import SESSION, BASE

class ForceSubscribe(BASE):
    __tablename__ = "forceSubscribe"
    chat_id = Column(BigInteger, primary_key=True)
    channel = Column(String, nullable=False)

    def __init__(self, chat_id, channel):
        self.chat_id = chat_id
        self.channel = channel

# Create table if not exists
ForceSubscribe.__table__.create(checkfirst=True)


# Get settings for a chat
def fs_settings(chat_id):
    try:
        return SESSION.query(ForceSubscribe).filter_by(chat_id=chat_id).one_or_none()
    except SQLAlchemyError as e:
        print(f"[DB ERROR] fs_settings: {e}")
        return None

# Add or update a channel for a chat
def add_channel(chat_id, channel):
    try:
        entry = SESSION.query(ForceSubscribe).get(chat_id)
        if entry:
            entry.channel = channel
        else:
            entry = ForceSubscribe(chat_id, channel)
            SESSION.add(entry)
        SESSION.commit()
    except SQLAlchemyError as e:
        print(f"[DB ERROR] add_channel: {e}")
        SESSION.rollback()


# Remove a channel (disable force subscribe)
def disapprove(chat_id):
    try:
        entry = SESSION.query(ForceSubscribe).get(chat_id)
        if entry:
            SESSION.delete(entry)
            SESSION.commit()
    except SQLAlchemyError as e:
        print(f"[DB ERROR] disapprove: {e}")
        SESSION.rollback()
