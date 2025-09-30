EP3 – Testes da API
Descrição do Projeto

Este projeto é uma API simples feita com FastAPI e Pydantic.
O objetivo é testar os endpoints com testes manuais e automatizados, verificando se a API funciona corretamente e como os testes ajudam a melhorar a qualidade do software.

Como instalar e rodar

Clonar o repositório:

git clone <link-do-repositorio>
cd ep2_api/ep2_api


Criar e ativar a virtualenv (Windows):

python -m venv .venv
.venv\Scripts\activate


Linux/Mac:

python3 -m venv .venv
source .venv/bin/activate


Instalar dependências:

pip install -r requirements.txt


Rodar a API:

uvicorn main:app --reload


A API ficará disponível em http://127.0.0.1:8000

Documentação automática em http://127.0.0.1:8000/docs

Testes Automatizados
Como rodar:
pytest -q

Testes feitos:
Teste	O que verifica
test_get_root	Se a rota / retorna a mensagem de boas-vindas
test_get_items_initial	Se /items retorna a lista de itens
test_post_item_success_and_presence	Criação de item e verificação na lista
test_post_item_missing_field	Validação de campos obrigatórios (quantidade)
test_docs_available	Se a documentação /docs está disponível

✅ Todos os testes passaram.

Casos de Teste Manuais
Caso	Cenário	Entrada	Passos	Resultado Esperado
1	Criar item válido	{"nome": "ItemTeste", "quantidade": 5}	POST /items com JSON	Status 200/201, mensagem de sucesso, item aparece na lista
2	Criar item sem campo obrigatório	{"nome": "ItemInvalido"}	POST /items com JSON	Status 400/422, mensagem de erro de campo obrigatório
3	Listar itens	Nenhuma	GET /items	Status 200, lista de itens retornada
4	Acessar página raiz	Nenhuma	GET /	Status 200, JSON {"mensagem": "Bem-vindo à API de itens!"}
5	Acessar documentação	Nenhuma	GET /docs	Status 200, interface Swagger carregada
Reflexão sobre qualidade do software

Testes ajudam a evitar erros antes que os usuários encontrem problemas.

Garantem que a API funcione conforme esperado.

Contribuem para sistemas mais confiáveis, seguros e estáveis.

Importante para que o software seja útil e seguro na prática para qualquer usuário.