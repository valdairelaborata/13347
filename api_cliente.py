
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cliente(BaseModel):
    id: int 
    nome: str
    email : str



@app.post("/cliente")
def criar_cliente(cliente: Cliente):
    return {"mensagem": f"Cliente {cliente.nome} - {cliente.email} incluído!"}


@app.get("/cliente")
def listar_cliente(nome, email):
    return {"mensagem": f"Cliente {nome} - {email} sendo pesquisado!"}


@app.get("/cliente/{id}")
def  buscar_cliente(id: int):
    return {"mensagem": f"Cliente {id} sendo buscado!"}


@app.put("/cliente/{id}")
def alterar_cliente(id: int, cliente: Cliente):
    return {"mensagem": f"Cliente {cliente.nome} - {cliente.email} sendo alterado!"}


@app.delete("/cliente/{id}")
def excluir_cliente(id: int):
    return {"mensagem": f"Cliente id:{id} sendo excluído!"}
