import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
import database
import models

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

models.Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

client = TestClient(app)

def test_criar_usuario():
    payload = {
        "id": 0,
        "nome": "João",
        "status": {
            "id": 1,
            "descricao": "string"

        }
    }
    response = client.post("/usuario/", json=payload)
    print(response.json())  
    assert response.status_code == 200
    # data = response.json()
    # assert data["nome"] == "João"
    # assert data["status"]["descricao"] == "Ativo"
    # assert "id" in data
    # assert "id" in data["status"]


def test_obter_usuario():
    payload = {
        "id": 0,
        "nome": "João",
        "status": {
            "id": 1,
            "descricao": "string"
        }
    }
    client.post("/usuario/", json=payload)

    
    # response = client.get("/usuario/2")  
    # assert response.status_code == 200
    # data = response.json()
    # assert data["nome"] == "Maria"
    # assert data["status"]["descricao"] == "Inativo"
