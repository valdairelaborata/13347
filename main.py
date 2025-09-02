
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

usuarios: list[Usuario] = []

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

@app.get("/usuario/{id}")
def obter_usuario(id: int):
    try:
        usuario = usuarios[0]
        return usuario
    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao obter usuario!!") 
    

@app.get("/usuario")
def obter_usuario_qs(id, cpf, idade):
    return {"mensagem": f"Usuário {id} - {cpf} - {idade}"}

@app.put("/usuario")
def alterar_usuario_body(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} - {usuario.email} alterado!"}

@app.delete("/usuario")
def excluir_usuario_body(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} - {usuario.email} alterado!"}

