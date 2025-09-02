EP2 - API do Projeto
Sobre a API

Esta API foi desenvolvida como entregável parcial 2 (EP2) e possui três rotas principais:

GET / → Mensagem de boas-vindas

GET /items → Lista de itens

POST /items → Criação de um novo item

Como executar

Ativar o ambiente virtual:
.\venv\Scripts\Activate # Windows
ou
source venv/bin/activate # Linux/Mac

Instalar dependências:
pip install fastapi uvicorn

Rodar a API:
uvicorn main:app --reload

Acesse a API em: http://127.0.0.1:8000/

Documentação interativa (Swagger UI): http://127.0.0.1:8000/docs

Exemplos de requisição e resposta
GET /

Requisição: GET http://127.0.0.1:8000/

Resposta: {"mensagem":"Bem-vindo à nossa API do EP2!"}

GET /items

Requisição: GET http://127.0.0.1:8000/items

Resposta: {"itens":["Item 1","Item 2","Item 3"]}

POST /items

Requisição: POST http://127.0.0.1:8000/items

Content-Type: application/json
{"nome": "Item Novo","quantidade": 10}
Resposta: {"mensagem": "Item criado com sucesso!","item": {"nome": "Item Novo","quantidade": 10}}

## Possíveis usos da nossa API

Esta API pode ser utilizada por pequenas empresas ou desenvolvedores para:

- **Gerenciar listas de itens e estoque** de maneira rápida, sem precisar de sistemas complexos.  
- **Criar protótipos de aplicativos ou websites**, simulando funcionalidades de cadastro e consulta de produtos.  
- **Automatizar processos de inventário**, por exemplo, registrando novos itens via formulários online.  
- **Treinar aprendizado de APIs REST**, permitindo que estudantes ou iniciantes pratiquem requisições GET e POST.  

Mesmo sendo simples, a API pode ser expandida para suportar **atualização (PUT), remoção (DELETE) e autenticação**, tornando-a útil para sistemas de vendas, controle de produtos ou qualquer aplicação que precise de gerenciamento básico de dados.
