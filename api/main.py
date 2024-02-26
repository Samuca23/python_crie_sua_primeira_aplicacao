from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def heloo_word() :
    """
    Endpoint que exibe uma mensagem incrível do mundo da programação
    """
    return {'Hello':'Word'}

@app.get('/api/restaurantes/')
def restaurantes(rst: str = Query(None)) :
    """
    Endpoint para verificar os cardápios dos restaurantes
    """
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200 :
        dados_json = response.json()

        if rst is None:
            return {'Dados': dados_json}

        dados_restaurante = []

        for item in dados_json :

            if item['Company'] == rst :
                dados_restaurante.append({
                    "item":item['Item'],
                    "price":item['price'],
                    "description":item['description']
                })
        return {'Restaurante': rst, 'Cardapio': dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}