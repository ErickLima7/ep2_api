from fastapi import FastAPI

app = FastAPI()

# Rota 1 - Home
@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à nossa API do EP2!"}

# Rota 2 - Lista de itens (GET)
@app.get("/items")
def get_items():
    return {"itens": ["Item 1", "Item 2", "Item 3"]}

# Rota 3 - Criar item (POST)
@app.post("/items")
def create_item(item: dict):
    return {"mensagem": "Item criado com sucesso!", "item": item}
