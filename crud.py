from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas


def criar_usuario(db: Session, usuario: schemas.Usuario):
    usuario_data = models.Usuario_data(nome=usuario.nome, status_id=usuario.status.id)
    db.add(usuario_data)
    db.commit()
    db.refresh(usuario_data)
    return usuario_data


def listar_usuarios(db: Session):
    return db.query(models.Usuario_data).all()


def obter_usuario(db: Session, id: int):
    usuario = db.query(models.Usuario_data).filter(models.Usuario_data.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!!")
    return usuario


def obter_usuario_por_nome(db: Session, nome: str):
    return db.query(models.Usuario_data).filter(models.Usuario_data.nome.ilike(f"%{nome}%")).all()


def alterar_usuario(db: Session, id: int, usuario: schemas.Usuario):
    usuario_data = db.query(models.Usuario_data).filter(models.Usuario_data.id == id).first()
    if not usuario_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!!")

    usuario_data.nome = usuario.nome
    usuario_data.status_id = usuario.status.id
    db.commit()
    db.refresh(usuario_data)
    return usuario_data


def excluir_usuario(db: Session, id: int):
    usuario_data = db.query(models.Usuario_data).filter(models.Usuario_data.id == id).first()
    if not usuario_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!!")
    db.delete(usuario_data)
    db.commit()
    return {"Mensagem": "Usuário excluído com sucesso"}


def criar_status(db: Session):
    status_padrao = ["Ativo", "Inativo"]
    for descricao in status_padrao:
        db.add(models.Status_data(descricao=descricao))
    db.commit()
    return {"Mensagem": "Status criado!"}
