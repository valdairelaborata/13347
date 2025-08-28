
from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()


class Usuario(BaseModel):
    nome: str
    email: str
    idade: int



@app.get("/cep")
def busca_cep(cep: str):
    url_via_cep = f"https://viacep.com.br/ws/{cep}/json/"  
    response = requests.get(url_via_cep)

    if response.status_code == 200:
        data = response.json()

        return {"mensagem": f"Dados do cep: {cep} - Logradouro: {data['logradouro']} - Bairro: {data['bairro']}"}
    else:
        return {"mensagem": f"Erro ao consultar cep: {cep}"}


@app.get("/usuario/{id}")
def obter_usuario(id: int):
    return {"mensagem": f"Usuário {id}"}

@app.get("/usuario")
def obter_usuario_qs(id, cpf, idade):
    return {"mensagem": f"Usuário {id} - {cpf} - {idade}"}


@app.post("/usuario")
def incluir_usuario_body(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} - {usuario.email} incluído!"}


@app.put("/usuario")
def alterar_usuario_body(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} - {usuario.email} alterado!"}


@app.delete("/usuario")
def excluir_usuario_body(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} - {usuario.email} alterado!"}

