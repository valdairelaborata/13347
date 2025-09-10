from pydantic import BaseModel

class Status(BaseModel):
    id: int
    descricao: str

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: int
    nome: str
    status: Status

    class Config:
        orm_mode = True
