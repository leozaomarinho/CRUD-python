# CRUD-python

📝 📌 Documentação do Projeto
#️⃣ 1. Título
Cadastro de Produtos e Gerenciamento de Estoque (Python MVC)

📄 2. Descrição do Projeto
Este projeto é um sistema de CRUD para cadastro de produtos e gerenciamento de estoque, implementado com a arquitetura MVC (Model-View-Controller) em Python, visando organizar as responsabilidades e facilitar futuras evoluções como integração com banco de dados e API REST.

🧩 3. Funcionalidades
✅ Cadastrar produtos com ID, nome, preço e quantidade

✅ Listar todos os produtos

✅ Atualizar dados do produto

✅ Remover produtos do estoque

✅ Ajustar quantidade de estoque (entrada e saída)

🏗️ 4. Arquitetura do Projeto (MVC)

Camada	Descrição
Model	Classes de dados e regras de negócio (Produto, EstoqueModel).
View	Interface CLI com usuário (EstoqueView).
Controller	Processa ações do usuário e conecta Model e View (EstoqueController).

💻 5. Tecnologias Utilizadas
Python 3.10+

SQLAlchemy (próxima etapa)

FastAPI (próxima etapa)

UML com PlantUML

pytest (testes futuros)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Crud utilizando arquitetura MVC

+-------------------+
|     Produto       |    <<Model>>
+-------------------+
| - id: str         |
| - nome: str       |
| - preco: float    |
| - quantidade: int |
+-------------------+
| + __init__()      |
| + __str__()       |
+-------------------+

        ^
        |
        | contém
        |

+-------------------+
|    Estoque        |    <<Model>>
+-------------------+
| - produtos: dict  |
+-------------------+
| + adicionar_produto()   |
| + listar_produtos()     |
| + atualizar_produto()   |
| + remover_produto()     |
| + ajustar_estoque()     |
+-------------------+

        ^
        |
        | usa
        |

+------------------------+
| EstoqueController      |    <<Controller>>
+------------------------+
| - model: Estoque       |
| - view: EstoqueView    |
+------------------------+
| + iniciar()            |
| + processar_opcao()    |
+------------------------+

        ^
        |
        | exibe
        |

+-------------------+
|  EstoqueView      |    <<View>>
+-------------------+
| + menu()          |
| + mostrar_produto()|
| + mostrar_lista()  |
| + mostrar_mensagem()|
+-------------------+