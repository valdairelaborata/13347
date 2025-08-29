
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import requests

app = FastAPI()


class Usuario(BaseModel):
    id: int
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

        usuarios.append(usuario)

        return usuario
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

