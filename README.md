# CRUD-python
repositorio para treino em python


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