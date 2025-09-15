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

def test_criar_usuario_status_code():
    payload = {
        "id": 0,
        "nome": "João",
        "status_id": 1
    }
    response = client.post("/usuario/", json=payload)
    response_json = response.json()

    # try:
    #     response_json = response.json()
    # except Exception as e:
    #     response_json = None
    #     print("Erro ao decodificar JSON:", e)
    
    if response_json:
        assert response_json.get("nome") == "João"
    
    assert response.status_code == 200
