from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import engine, SessionLocal, Base
from sqlalchemy import text

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))  # simple test query
        return {"message": "Database connection successful!"}
    except Exception as e:
        return {"error": str(e)}
