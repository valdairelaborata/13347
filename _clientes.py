from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()


SQLALCHEMY_DATABASE_URL = "sqlite:///./clientes_.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

class Cliente_Data(Base):
    __tablename__ ="clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String )
    telefone = Column(String)
    idade = Column(Integer)
    cidade = Column(String)




Base.metadata.create_all(engine)


class Cliente(BaseModel):
    id: int 
    nome: str
    email : str
    telefone: str
    idade: int
    cidade: str


@app.post("/cliente", 
          response_model= Cliente,
          tags= ["Cliente"],
          summary= "Criar um registro de cliente.",
          description="End.point para um novo registro de usuario",
          responses= {500:{"description": "Erro ao criar cliente"}}
          )

def criar_cliente(cliente: Cliente):
    
    try:
        conn = SessionLocal()


        cliente_data = Cliente_Data(nome = cliente.nome, email = cliente.email, telefone = cliente.telefone, idade = cliente.idade ,cidade = cliente.cidade)



        conn.add(cliente_data)
        conn.commit()
        conn.refresh(cliente_data)
        conn.close()
       
        return cliente_data
    except Exception as ex:
        # fazer algum log
        raise HTTPException(status_code=500, detail=f"Erro ao criar cliente{ex}")
    

@app.get("/cliente", 
         response_model= Cliente,
          tags= ["Cliente"],
          summary= "Listar clientes com base em nos parametros.",
          description="End.point para listagem dos clientes",
          responses= {500:{"description": "Erros ao listar clientes"}})

def listar_cliente(nome, email):
    try:
    
        cliente= Cliente()
        cliente.nome
        cliente.email
        return cliente
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Erro ao listar clientes")


# @app.get("/cliente/{id}",
#          response_model= Cliente,
#          tags= ["Cliente"],
#          summary= "buscar cliente com base no id passado.",
#          description="Retorno de dados do cliente encontrado",
#          responses= {500:{ "Erros buscar regitro do cliente"}})

# def  buscar_cliente(id: int):
#     try:
#         db = SessionLocal()
#         cliente= db.query(Cliente_Data).filter(Cliente_Data.id == id).first()
#         db.close()

#         if not cliente:
#             raise HTTPException(status_code=404, detail=f"Nao existe cliente com o id informado{ex}")
        
#         return cliente
    
#     except Exception as ex:
#         raise HTTPException(status_code=500, detail="Erro ao buscar cliente")



@app.get("/cliente/{id}",
          response_model= Cliente,
          tags=["Cliente"],
          summary="Buscar cliente com base no id passado.",
          description="End-point para retornar os dados do cliente encontrado.",
          responses={500:{"description": "Erro ao buscar registro de cliente."}})
def  buscar_cliente(id: int):
    try:
        db =  SessionLocal()        
        cliente = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()
        db.close()

        if not cliente:
          raise HTTPException(status_code=404, detail=f"Não existe cliente com o id informado!")

        return cliente
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar cliente {ex}.")



@app.put("/cliente/{id}",
         response_model= Cliente,
          tags= ["Cliente"],
          summary= "Alterar de cliente.",
          description="Altero registro de cliente",
          responses= {500:{"description": "Erro ao alterar registro de cliente"}})

def alterar_cliente(id: int, cliente: Cliente):
        db = SessionLocal()

        cliente = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()

        if not cliente:
            raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 


        cliente.nome = cliente.nome

        db.commit()
        db.refresh(cliente)

        db.close()

        return cliente


@app.delete("/cliente/{id}",
          tags= ["Cliente"],
          summary= "Excluir cliente.",
          description="Excluir registro de cliente",
          responses= {500:{"description": "Erro ao excluir cliente !!"}})

def excluir_cliente(id):
    try:
    
        db = SessionLocal()
        cliente_data = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()
        
        if not cliente_data:
            raise HTTPException(status_code=404, detail=f"Cliente nao encontrado")
        
        
        db.delete = (cliente_data)
        
        
        db.commit()
        db.close()


        return {"Mensagem": "Cliente excluido com sucesso"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir cliente")