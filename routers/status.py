from fastapi import APIRouter, Depends, HTTPException


from crud import criar_status
from database import get_db


router = APIRouter(prefix="/status", tags=["Status"])


@router.post("/",               
          summary="Criar status",
          description="Cria status de usuário caso passar pelas regras (detalhar regras)",
          responses={500:{"description": "Erro ao criar status!!"}}
          )
def criar(db = Depends(get_db)):
    try:
        return criar_status(db)
    
    except Exception as e:  
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao criar status!!") 
    


