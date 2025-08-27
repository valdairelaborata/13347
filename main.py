
from fastapi import FastAPI

app = FastAPI()

@app.get("/usuario")
def listar_usuarios():
    return {"mensagem": "Dados de usuário"}

@app.get("/usuario/{id}")
def obter_usuario(id: int):
    return {"mensagem": f"Usuário {id}"}

@app.get("/usuario/cpf/{cpf}")
def obter_usuario_por_cpf(cpf: str):
    return {"mensagem": f"Usuário localizado com o cpf: {cpf}"}


@app.get("/opa")
def teste02():
    return {"mensagem": "Opa!"}

