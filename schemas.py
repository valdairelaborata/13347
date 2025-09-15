from pydantic import BaseModel


class Status(BaseModel):
        id: int
        descricao: str
     
class Usuario(BaseModel):
    id: int
    nome: str    
    status_id: int
   
