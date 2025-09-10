from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter(prefix="/usuario", tags=["Usuários"])

@router.post("/", response_model=schemas.Usuario)
def criar(usuario: schemas.Usuario, db: Session = Depends(database.get_db)):
    return crud.criar_usuario(db, usuario)

@router.get("/", response_model=list[schemas.Usuario])
def listar(db: Session = Depends(database.get_db)):
    return crud.listar_usuarios(db)

@router.get("/buscar", response_model=list[schemas.Usuario])
def buscar_por_nome(nome: str, db: Session = Depends(database.get_db)):
    return crud.obter_usuario_por_nome(db, nome)

@router.get("/{id}", response_model=schemas.Usuario)
def obter(id: int, db: Session = Depends(database.get_db)):
    return crud.obter_usuario(db, id)

@router.put("/{id}", response_model=schemas.Usuario)
def alterar(id: int, usuario: schemas.Usuario, db: Session = Depends(database.get_db)):
    return crud.alterar_usuario(db, id, usuario)

@router.delete("/{id}")
def excluir(id: int, db: Session = Depends(database.get_db)):
    return crud.excluir_usuario(db, id)
