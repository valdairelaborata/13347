from fastapi import FastAPI
from database import Base, engine
from routers import usuarios, status


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(usuarios.router)
app.include_router(status.router)
