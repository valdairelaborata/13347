Sistema de Pedidos de Restaurante

Descritivo:
Um sistema para gerenciar pedidos de um restaurante. Permite cadastrar clientes, pratos e categorias, registrar pedidos com múltiplos itens e acompanhar o status de cada pedido. 

Cliente (id, nome, telefone, email)
Prato (id, nome, preco, categoria_id)
Categoria de Prato (id, nome)
Pedido (id, cliente_id, data_pedido, status)
ItemPedido (id, pedido_id, prato_id, quantidade)

Funcionalidades:
CRUD de clientes, pratos e categorias.
Registrar pedidos com múltiplos pratos e quantidades.
Atualizar status do pedido (em preparo, pronto, entregue).
Consultar pedidos por cliente ou status.