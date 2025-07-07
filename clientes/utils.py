import requests

def buscar_personagem_dbz(nome):
    """Busca dados do personagem na Dragon Ball API pelo nome"""
    url = f'https://dragonball-api.com/api/characters?name={nome}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Pode ser um dict (com chave 'items') ou já uma lista
            if isinstance(data, dict) and 'items' in data:
                items = data['items']
            elif isinstance(data, list):
                items = data
            else:
                items = []
            if items:
                return items[0]
    except Exception as e:
        print(f"Erro ao consultar Dragon Ball API: {e}")
    return None
