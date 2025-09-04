
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import requests

app = FastAPI()


SQLALCHEMY_DATABASE_URL = "sqlite:///./usuarios.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

class Usuario_data(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False )



Base.metadata.create_all(engine)

class Usuario(BaseModel):
    id: int
    nome: str

@app.get("/cep")
def busca_cep(cep: str):
    url_via_cep = f"https://viacep.com.br/ws/{cep}/json/"  
    response = requests.get(url_via_cep)

    if response.status_code == 200:
        data = response.json()

        return {"mensagem": f"Dados do cep: {cep} - Logradouro: {data['logradouro']} - Bairro: {data['bairro']}"}
    else:
        return {"mensagem": f"Erro ao consultar cep: {cep}"}


@app.post("/usuario",
          response_model=Usuario,
          tags=["Usuários"],
          summary="Criar um registro de usuário",
          description="Cria um registro de usuário caso passar pelas regras (detalhar regras)",
          responses={500:{"description": "Erro ao criar usuario!!"}}
          )
def criar_usuario(usuario: Usuario):
    try:

        usuario_data = Usuario_data(nome = usuario.nome)

        db = SessionLocal()
        db.add(usuario_data)
        db.commit()
        db.refresh(usuario_data)
        db.close()

        return usuario_data
    
    except Exception as e:  
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuario!!") 


@app.get("/usuario",
          response_model=Usuario,
          tags=["Usuários"],
          summary="Listar usuários",
          description="Listagem de usuários",
          responses={500:{"description": "Erro ao listar usuarios!!"}}
          )
def listar_usuario():
    try:
        db = SessionLocal()
        usuarios = db.query(Usuario_data).all()
 

        db.close()

        return usuarios
        
    except Exception as e:  
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuarios: {e}!!") 




@app.get("/usuario/{id}",
          response_model=Usuario,
          tags=["Usuários"],
          summary="Obter usuário",
          description="Busacar um usuário",
          responses={500:{"description": "Erro ao buscar usuario!!"}}
          )
def obter_usuario(id: int):
    try:

        db = SessionLocal()
        usuario = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        db.close()


        if not usuario:
           raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 
   

        return usuario
    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao obter usuario{e}!!") 
    
@app.put("/usuario/{id}",
          response_model=Usuario,
          tags=["Usuários"],
          summary="Alterar usuário",
          description="Altero um registro de usuário",
          responses={500:{"description": "Erro ao alterar usuario!!"}}
         )
def alterar_usuario(id: int, usuario: Usuario):
    try:
        db = SessionLocal()

        usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        if not usuario_data:
            raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 


        usuario_data.nome = usuario.nome

        db.commit()
        db.refresh(usuario_data)

        db.close()

        return usuario_data

    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao alterar usuario{e}!!") 
    

@app.delete("/usuario/{id}",            
          tags=["Usuários"],
          summary="Excluir usuário",
          description="Excluir um registro de usuário",
          responses={500:{"description": "Erro ao excluir usuario!!"}}
          )
def excluir_usuario_body(id: int):
    try:
        db = SessionLocal()
        usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        if not usuario_data:
           raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 
     
        db.delete(usuario_data)
        db.commit()
        db.close()

        return {"Mensagem": "Usuário excluido com sucesso"}

    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao excluir usuario{e}!!") 
    

    

