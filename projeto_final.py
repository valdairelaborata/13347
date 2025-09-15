from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()

Minha_URL_DATABASE = "sqlite:///./restaurante.db"

engine = create_engine(Minha_URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()




class Cliente_data(Base):
    __tablename__ = "Clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)


Base.metadata.create_all(engine)


class Cliente(BaseModel):
    id: int
    nome: str
    telefone: str

def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()



@app.post("/cliente",
          response_model=Cliente,
          tags=["Clientes"],
          summary="Criar um registro de cliente",
          description="Cria um registro de cliente caso passar pela verificaçao de login",
          responses={500:{"description": "Erro ao criar registro de cliente!!"}})
def criar_cliente(cliente: Cliente, db = Depends (get_db)):
    try:
        cliente_data = Cliente_data(nome = cliente.nome, telefone = cliente.telefone)
        

        db.add(cliente_data)
        db.commit()
        db.refresh(cliente_data)
        db.close()

        return cliente_data
    
    except Exception as e:   
        raise HTTPException(status_code=500, detail=f"Erro ao criar cliente{e}!!") 


@app.get("/cliente/{id}", 
        response_model=Cliente,
        tags=["Clientes"],
        summary="Buscar cliente pelo id",
        description="Busca um cliente com base no seu id",
        responses={500:{"description": "Erro ao buscar cliente!!"}})
def buscar_cliente_pelo_id(id: int, db = Depends(get_db)):
    try:
        clientes = db.query(Cliente_data).filter(Cliente_data.id == id).first()

        if not clientes:
            raise HTTPException(status_code=404, detail="Registro de cliente não encontrado")
    
        return clientes
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Erro ao encontrar cliente")

@app.put("/cliente/{id}/",
        response_model=Cliente,
        tags=["Clientes"],
        summary="Alterar cliente pelo id",
        description="Altera o registro de um cliente pelo id",
        responses={500:{"description": "Erro ao alterar registro de cliente cliente!!"}})
def alterar_cliente(id: int, cliente: Cliente ,db = Depends(get_db)):
    try:
        clientes_data = db.query(Cliente_data).filter(Cliente_data.id == id).first()

        if not clientes_data:
            raise HTTPException(status_code=404, detail= "Erro ao alterar registro de cliente")
   
        clientes_data.nome = cliente.nome

        db.commit()
        db.refresh(clientes_data)

        return clientes_data
   
   
   
   
   
   
   
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao alterar cliente")

@app.delete("/cliente/{id}/",
        tags=["Clientes"],
        summary="Deletar cliente pelo id",
        description="Deleta um cliente com base no seu id",
        responses={500:{"description": "Erro ao deletar cliente!!"}})
def deletar_cliente(id: int, db = Depends(get_db)):
    # try:
    clientes_data = db.query(Cliente_data).filter(Cliente_data.id == id).first()

    if not clientes_data:
        raise HTTPException(status_code=404, detail="Erro ao deletar registro cliente")
        
       

    db.delete(clientes_data)
    db.commit()
        

    return ("mensagem: Cliente excluido com sucesso")
    
    
    
    
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Erro ao deletar cliente{e}")

