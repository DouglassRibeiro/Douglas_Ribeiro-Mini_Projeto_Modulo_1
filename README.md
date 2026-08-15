# organizar_texto_categoria

Foi definido antes de tudo nomes vazios como 'sem categoria' evitando travar o sistema com categorias nulas. 

```python
if not texto or texto.strip() == '': # economia, somente 'se texto for nulo ou não tiver nada' entraria nesse laço ignorando os demais
    return 'sem categoria'
```
No demais 
```python
...
texto_limpo = texto.lower().strip() # padronizando e limpando espaços de inicio e fim desnecessários

texto_limpo = re.sub(r'[^a-z0-9_\s]', '', texto_limpo) # Regex reorganiza caracteres: r[^\s] o ^ significa qualquer coisa que não esteja aqui, \s para não apagar espaços em branco 

return texto_limpo # retorne texto limpo
```

# tratar_dimensoes_fisicas

Definindo blocos númericos vazios como 0.0 ou float

```python
campos_dimensoes = [
    'product_name_lenght',
    'product_description_lenght',
    'product_photos_qty',
    'product_weight_g',
    'product_length_cm', 
    'product_height_cm',
    'product_width_cm'
]

for campo in campos_dimensoes: # verificando linha por linha e convertendo valores numéricos que em planilhas estão definidas como string normal para valores float
    valor = produto.get(campo)

    if valor is None or valor.strip() == '': # e claro não esquecer dos Nulos
        produto[campo] = 0.0
    else:
        produto[campo] = float(valor) 

return produto
```

# filtro_validacao

Comparando o por que "order_delivered_customer_data" esta vazia com os demais status no "order_status".

```python
def filtro_validação(lista_pedidos):

    cancelados = 0
    total_sem_entrega = 0
    outros_status = 0

    campos_dimensoes = [
        'order_delivered_customer_date',
        'order_status'
    ]

    for pedido in lista_pedidos:
        data_entrega = pedido.get('order_delivered_customer_date')
        status = pedido.get('order_status')

        # 1. Checa se a data de entrega é nula/vazia
        if not data_entrega or data_entrega.strip() == '':
            total_sem_entrega += 1  # Soma +1 para qualquer entrega vazia

            # 2. Classifica o motivo
            if status == 'canceled':
                cancelados += 1
            else:
                outros_status += 1

    return total_sem_entrega, cancelados, outros_status
```