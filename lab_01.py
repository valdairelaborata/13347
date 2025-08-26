
import requests

def consulta_cep(cep):
    url =f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"CEP: {data['cep']}")
        print(f"Logradouro: {data['logradouro']}")
        print(f"Bairro: {data['bairro']}")
        

consulta_cep("81710230")