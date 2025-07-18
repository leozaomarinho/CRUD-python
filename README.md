# CRUD-python
repositorio para treino em python


Crud utilizando arquitetura MVC

Recursos 
+----------------+
|   Produto      |    <<Model>>
+----------------+
| - id: str      |
| - nome: str    |
| - preco: float |
| - quantidade: int |
+----------------+
| + __init__()   |
| + __str__()    |
+----------------+

+----------------+
|   EstoqueModel |   <<Model>>
+----------------+
| - produtos: dict|
+----------------+
| + adicionar()  |
| + listar()     |
| + atualizar()  |
| + remover()    |
| + ajustar_estoque() |
+----------------+

+----------------+
|   EstoqueView  |   <<View>>
+----------------+
| + menu()       |
| + mostrar_produto() |
| + mostrar_lista() |
| + mostrar_mensagem() |
+----------------+

+----------------+
| EstoqueController | <<Controller>>
+----------------+
| - model: EstoqueModel |
| - view: EstoqueView |
+----------------+
| + iniciar()    |
| + processar_opcao() |
+----------------+

