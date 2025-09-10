
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Usuario_data(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False )
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)

    status = relationship("Status_data")



class Status_data(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False )
