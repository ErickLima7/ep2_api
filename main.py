from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Modelo de Item
class Item(BaseModel):
    nome: str = Field(..., example="Exemplo de item")
    quantidade: int = Field(..., ge=1, example=3)

# Lista interna para armazenar itens
items: List[Item] = []

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API de itens!"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"mensagem": "Item criado com sucesso!", "item": item}
