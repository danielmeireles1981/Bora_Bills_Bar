# 🍹 Bora Bills Bar

**O bar cósmico do universo Dragon Ball Z, feito em Django!**

---

## Descrição

O **Bora Bills Bar** é um sistema web temático desenvolvido em Django, inspirado no personagem Bills, o Deus da Destruição de Dragon Ball Z. O projeto une criatividade, integração com APIs externas e um visual moderno, gamificando a experiência do usuário em um bar fictício com ranking de clientes, cardápio dinâmico, curiosidades e previsão do tempo.

---

## Funcionalidades

- **Cardápio de Drinks Cósmicos:** Busca de bebidas na [TheCocktailDB API](https://www.thecocktaildb.com/api.php), com fotos, ingredientes e modo de preparo.
- **Ranking de Clientes:** Sistema de pontos, avatares e ranqueamento dos melhores clientes.
- **Personagem Favorito:** Associe um personagem de Dragon Ball ao perfil do cliente, com imagem e curiosidades.
- **Curiosidades Dragon Ball:** Página interativa puxando fatos aleatórios da [Dragon Ball API](https://dragonball-api.com/).
- **Previsão do Tempo:** Mostra o clima atual em qualquer cidade, via Open-Meteo API.
- **Painel administrativo:** Gerenciamento de clientes pelo Django Admin.

---

## Pré-requisitos

- Python 3.8+
- Django 4+ ou 5+
- Pip
- (Opcional) Virtualenv

---

## Instalação

```bash
# Clone este repositório
git clone https://github.com/seuusuario/bora-bills-bar.git
cd bora-bills-bar

# Crie o ambiente virtual (recomendado)
python -m venv venv
# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

Se não existir o arquivo `requirements.txt`, crie um assim:

```txt
Django>=4.0
requests
```

---

## Rodando o projeto

```bash
python manage.py migrate
python manage.py runserver
```

Abra seu navegador em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Principais Endpoints

* `/` — Página inicial (home), previsão do tempo
* `/cardapio/` — Cardápio de drinks dinâmico
* `/curiosidades/` — Curiosidades Dragon Ball (personagens aleatórios ou por busca)
* `/clientes/ranking/` — Ranking dos clientes

---

## Como cadastrar clientes

1. Acesse o painel admin:
   [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```
3. Cadastre clientes, incluindo nome, e-mail, pontos, avatar e personagem favorito.

---

## Estrutura de Pastas

```
bora_bills_bar/
├── core/
├── menu/
│   └── templates/
│       └── menu/
├── clientes/
│   └── templates/
│       └── clientes/
├── api/
├── static/
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## Integrações

* **TheCocktailDB:** drinks, fotos e receitas.
* **Dragon Ball API:** informações de personagens.
* **Open-Meteo:** previsão do tempo mundial, geocoding para cidades.

---

## Créditos e Licença

* Projeto acadêmico, livre para uso e aprendizado.
* APIs públicas utilizadas (consulte os termos das APIs).
* Tema Dragon Ball Z © Akira Toriyama / Toei Animation (uso não comercial/educacional).

---

## Contribuindo

Pull requests e sugestões são bem-vindos!
Abra uma issue ou envie seu PR.

---

**Desenvolvido por Daniel Meireles do Rego(https://github.com/danielmeireles1981) — 2025**

---
