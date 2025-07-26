from sqlalchemy.orm import Session
from . import models

def create_user_if_not_exists(db: Session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        user = models.User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def create_session(db: Session, user_id: int):
    session = models.ConversationSession(user_id=user_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def store_message(db: Session, session_id: int, role: str, content: str):
    message = models.Message(session_id=session_id, role=role, content=content)
    db.add(message)
    db.commit()
    return message
