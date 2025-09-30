import sys
import os
import uuid
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_get_root():
    res = client.get("/")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)
    assert "mensagem" in data

def test_get_items_initial():
    res = client.get("/items")
    assert res.status_code == 200
    data = res.json()
    if isinstance(data, list):
        assert True
    else:
        assert "itens" in data and isinstance(data["itens"], list)

def test_post_item_success_and_presence():
    nome_unico = f"Item-{uuid.uuid4().hex[:6]}"
    payload = {"nome": nome_unico, "quantidade": 3}
    res = client.post("/items", json=payload)
    assert res.status_code in (200, 201)
    body = res.json()
    assert any(k in body for k in ("mensagem", "item", "id"))

    res2 = client.get("/items")
    data2 = res2.json()
    items = data2 if isinstance(data2, list) else data2.get("itens", [])
    found = any(
        (isinstance(it, dict) and it.get("nome") == nome_unico) or it == nome_unico
        for it in items
    )
    assert found, "O item criado não foi encontrado na listagem."

def test_post_item_missing_field():
    payload = {"nome": "Só Nome"}
    res = client.post("/items", json=payload)
    assert res.status_code in (400, 422)

def test_docs_available():
    res = client.get("/docs")
    assert res.status_code == 200
    assert "text/html" in res.headers.get("content-type", "")
