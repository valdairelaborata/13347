
from fastapi import HTTPException
from sqlalchemy.orm import Session


from models import Status_data, Usuario_data
from schemas import Usuario


def criar_usuario(usuario: Usuario, db: Session):
        
    usuario_data = Usuario_data(nome = usuario.nome, status_id = usuario.status.id)

    db.add(usuario_data)
    db.commit()
    db.refresh(usuario_data)
    

    return usuario_data
    

def obter_usuario_por_nome(nome: str, db: Session):
    usuarios = db.query(Usuario_data).filter(Usuario_data.nome.ilike(f"%{nome}%")).all()      
    return usuarios 


def obter_usuario(id: int, db: Session):

    usuario = db.query(Usuario_data).filter(Usuario_data.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 
   
    return usuario

def alterar_usuario(id: int, usuario: Usuario, db: Session):

    usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

    if not usuario_data:
        raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 


        usuario_data.nome = usuario.nome
        usuario_data.status_id = usuario.status.id

        db.commit()
        db.refresh(usuario_data)

     
        return usuario_data



def excluir_usuario(id: int, db: Session):

    usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

    if not usuario_data:
        raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 
     
    db.delete(usuario_data)
    db.commit()
   

    return {"Mensagem": "Usuário excluido com sucesso"}



def criar_status(db: Session):
    status_padrao = ["Ativo", "Inativo"]
     
    for descricao in status_padrao:
        db.add(Status_data(descricao = descricao))
        
    db.commit()

    return {"Mensagem": "Status criado!" }
        
   