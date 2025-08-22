

def aplicar(funcao, valor):
    return funcao(valor)

def dobrar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

resultado = aplicar(dobrar, 5)
print(resultado)
resultado = aplicar(triplicar, 5)
print(resultado)

