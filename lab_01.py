
class Usuario:
    def __init__(self, nome, token):
        self.nome = nome
        self.token =  token

def valida_autenticacao(funcao):
    def wapper(usuario: Usuario):
        if usuario.token == "xpto050":
            print("Autenticado!!")
            funcao()
        else:
            print("Usuário não autenticado!!")

    return wapper
        

@valida_autenticacao
def consultar_produto():
    print("Aqui vai ser feita a consulta de produtos..")

@valida_autenticacao
def alterar_produto():
    print("Aqui vai ser feita a alteração de produtos..")


usuario = Usuario("user 01", "xpto050")
consultar_produto(usuario)
alterar_produto(usuario)

