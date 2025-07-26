from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models, crud, schemas, llm_integration

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/chat")
def chat(message: schemas.ChatRequest, db: Session = Depends(get_db)):
    # Ensure user exists
    user = crud.create_user_if_not_exists(db, username="default_user")

    # Create a session if not passed
    if not message.conversation_id:
        session = crud.create_session(db, user.id)
        conversation_id = session.id
    else:
        conversation_id = message.conversation_id

    # Store user message
    crud.store_message(db, conversation_id, role="user", content=message.message)

    # Generate AI response
    ai_response = llm_integration.generate_response(message.message)

    # Store AI response
    crud.store_message(db, conversation_id, role="ai", content=ai_response)

    return {"conversation_id": conversation_id, "response": ai_response}
