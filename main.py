
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/cep")
def busca_cep(cep: str):
    url_via_cep = f"https://viacep.com.br/ws/{cep}/json/"  
    response = requests.get(url_via_cep)

    if response.status_code == 200:
        data = response.json()

        return {"mensagem": f"Dados do cep: {cep} - Logradouro: {data['logradouro']} - Bairro: {data['bairro']}"}
    else:
        return {"mensagem": f"Erro ao consultar cep: {cep}"}


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

