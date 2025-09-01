
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Cliente(BaseModel):
    id: int 
    nome: str
    email : str



@app.post("/cliente",
          response_model= Cliente,
          tags=["Cliente"],
          summary="Criar um registro de cliente.",
          description="End-point para um novo registro de usuário com base nas informações inviadas.",
          responses={500:{"description": "Erro ao criar cliente!!"}}
          )
def criar_cliente(cliente: Cliente):
    try:
        return cliente    
    except Exception as ex:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail="Erro ao criar cliente.")


@app.get("/cliente",
          response_model= Cliente,
          tags=["Cliente"],
          summary="Listar os clientes com base nos parâmetros.",
          description="End-point para listagem de clientes.",
          responses={500:{"description": "Erros ao listar clientes!!"}})
def listar_cliente(nome, email):
    try:
        cliente = Cliente()
        cliente.nome = nome
        cliente.email = email
        return cliente
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Erro ao listar clientes.")


@app.get("/cliente/{id}",
          response_model= Cliente,
          tags=["Cliente"],
          summary="Buscar cliente com base no id passado.",
          description="End-point para retornar os dados do cliente encontrado.",
          responses={500:{"description": "Erro ao buscar registro de cliente."}})
def  buscar_cliente(id: int):
    try:
        cliente = Cliente()
        cliente.nome = "nome"
        cliente.email = "email"
        return cliente
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Erro ao buscar cliente.")



@app.put("/cliente/{id}",
          response_model= Cliente,
          tags=["Cliente"],
          summary="Alterar registro de cliente.",
          description="End-point para alterar cliente informado.",
          responses={500:{"description": "Erro ao alterar cliente!!"}})
def alterar_cliente(id: int, cliente: Cliente):
    try:
        cliente = Cliente()
        cliente.nome = "nome"
        cliente.email = "email"
        return cliente
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Erro ao alterar cliente.")


@app.delete("/cliente/{id}",
          response_model= Cliente,
          tags=["Cliente"],
          summary="Excluir registro de cliente.",
          description="End-point para excluir cliente informado.",
          responses={500:{"description": "Erro ao excluir cliente!!"}})
def excluir_cliente(id: int):
    try:
        cliente = Cliente()
        cliente.nome = "nome"
        cliente.email = "email"
        return cliente
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Erro ao excluir cliente.")

