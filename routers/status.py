from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, database

router = APIRouter(prefix="/status", tags=["Status"])

@router.post("/")
def criar(db: Session = Depends(database.get_db)):
    return crud.criar_status(db)
