
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def teste():
    return {"mensagem": "Teste de resquest no método GET"}
