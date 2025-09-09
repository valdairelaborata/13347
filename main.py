
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()


SQLALCHEMY_DATABASE_URL = "sqlite:///./usuarios.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

class Usuario_data(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False )
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)

    status = relationship("Status_data")




class Status_data(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False )



Base.metadata.create_all(engine)

class Status(BaseModel):
        id: int
        descricao: str


class Usuario(BaseModel):
    id: int
    nome: str
    status: Status



def get_db():
     db = SessionLocal()
     try:
         yield db
     finally:
         db.close()

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
def criar_usuario(usuario: Usuario, db = Depends(get_db)):
    try:
        
        usuario_data = Usuario_data(nome = usuario.nome, status_id = usuario.status.id)

        db.add(usuario_data)
        db.commit()
        db.refresh(usuario_data)
        

        return usuario_data
    
    except Exception as e:  
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuario!! {e}") 

# @app.get("/usuario",
#           response_model=list[Usuario],
#           tags=["Usuários"],
#           summary="Listar usuários",
#           description="Listagem de usuários",
#           responses={500:{"description": "Erro ao listar usuarios!!"}}
#           )
# def listar_usuario(db = Depends(get_db)):
#     try:
      
#         usuarios = db.query(Usuario_data).all()
#         return usuarios
        
#     except Exception as e:  
#         # Fazer algum log {e} 
#         raise HTTPException(status_code=500, detail=f"Erro ao listar usuarios: {e}!!") 



@app.get("/usuario/buscar",
          response_model=list[Usuario],
          tags=["Usuários"],
          summary="Obter usuário por parte do nome",
          description="Busacar um usuário",
          responses={500:{"description": "Erro ao buscar usuario!!"}}
          )
def obter_usuario_por_nome(nome: str, db = Depends(get_db) ):
    try:
        usuarios = db.query(Usuario_data).filter(Usuario_data.nome.ilike(f"%{nome}%")).all()      
        return usuarios 
        
    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao alterar usuario{e}!!") 

@app.get("/usuario/{id}",
          response_model=Usuario,
          tags=["Usuários"],
          summary="Obter usuário",
          description="Busacar um usuário",
          responses={500:{"description": "Erro ao buscar usuario!!"}}
          )
def obter_usuario(id: int, db = Depends(get_db) ):
    try:

        # db = SessionLocal()
        # usuario = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        # db.close()


        usuario = db.query(Usuario_data).filter(Usuario_data.id == id).first()

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
def alterar_usuario(id: int, usuario: Usuario, db = Depends(get_db)):
    try:
     
        usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        if not usuario_data:
            raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 


        usuario_data.nome = usuario.nome
        usuario_data.status_id = usuario.status.id

        db.commit()
        db.refresh(usuario_data)

     
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
def excluir_usuario_body(id: int, db = Depends(get_db)):
    try:
        
        usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        if not usuario_data:
           raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 
     
        db.delete(usuario_data)
        db.commit()
   

        return {"Mensagem": "Usuário excluido com sucesso"}

    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao excluir usuario{e}!!") 
    


@app.post("/status",     
          tags=["Status"],
          summary="Criar status",
          description="Cria status de usuário caso passar pelas regras (detalhar regras)",
          responses={500:{"description": "Erro ao criar status!!"}}
          )
def criar_status(db = Depends(get_db)):
    try:
        
        status_padrao = ["Ativo", "Inativo"]

        for descricao in status_padrao:
            db.add(Status_data(descricao = descricao))

        db.commit()


        return {"Mensagem": "Status criado!" }
    
    except Exception as e:  
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao criar status!!") 
    

