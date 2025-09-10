from fastapi import APIRouter, Depends, HTTPException

from crud import criar_usuario, excluir_usuario, obter_usuario, obter_usuario_por_nome
from database import get_db
from models import Usuario_data
from schemas import Usuario


router = APIRouter(prefix="/usuario", tags=["Usuários"])


@router.post("/",
          response_model=Usuario,          
          summary="Criar um registro de usuário",
          description="Cria um registro de usuário caso passar pelas regras (detalhar regras)",
          responses={500:{"description": "Erro ao criar usuario!!"}}
          )
def criar(usuario: Usuario, db = Depends(get_db)):
   return criar_usuario(usuario, db)


@router.get("/buscar",
          response_model=list[Usuario],
          summary="Obter usuário por parte do nome",
          description="Busacar um usuário",
          responses={500:{"description": "Erro ao buscar usuario!!"}}
          )
def obter_por_nome(nome: str, db = Depends(get_db) ):
    try:
        return obter_usuario_por_nome(nome, db)
        
    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao alterar usuario{e}!!") 


@router.get("/{id}",
          response_model=Usuario,
          summary="Obter usuário",
          description="Busacar um usuário",
          responses={500:{"description": "Erro ao buscar usuario!!"}}
          )
def obter(id: int, db = Depends(get_db) ):
    try:
        
        return obter_usuario(id, db)
        
    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao obter usuario{e}!!") 


@router.put("/{id}",
          response_model=Usuario,
          summary="Alterar usuário",
          description="Altero um registro de usuário",
          responses={500:{"description": "Erro ao alterar usuario!!"}}
         )
def alterar(id: int, usuario: Usuario, db = Depends(get_db)):
    try:
          
        usuario_data = db.query(Usuario_data).filter(Usuario_data.id == id).first()

        if not usuario_data:
            raise HTTPException(status_code=404, detail=f"Usuário não encontrado!!") 


        usuario_data.nome = usuario.nome
        usuario_data.status_id = usuario.status.id

        db.commit()
        db.refresh(usuario_data)
     
        return usuario_data
    

    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao alterar usuario{e}!!") 

@router.delete("/{id}",            
          summary="Excluir usuário",
          description="Excluir um registro de usuário",
          responses={500:{"description": "Erro ao excluir usuario!!"}}
          )
def excluir(id: int, db = Depends(get_db)):
    try:
              
       return excluir_usuario(id, db)

    except Exception as e:
        # Fazer algum log {e} 
        raise HTTPException(status_code=500, detail=f"Erro ao excluir usuario{e}!!") 
    


