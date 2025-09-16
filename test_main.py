from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

import models
from main import app
import database

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
    )


TestingSessionLocal = sessionmaker(autoflush=False, bind=engine)


models.Base.metadata.create_all(engine)


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
        "nome": "Luis",
        "status_id": 1
    }

    response = client.post("/usuario/", json=payload)

    assert response.status_code == 200

