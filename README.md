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

# formatacao_temporal

Utilizando datetime usei o .strftime para gerar strings legiveis da "planilha olist_orders-dataset.csv" na coluna "order_approved_at" e assim convertendo o formato original oferecido para pt-br apresentando seus dados.

```python
def formatacao_temporal(data): # %H:%M:%S: Horas, minutos e segundos | %Y: Ano , %m: Mês, %d: Dia

    if not data or data.strip() == '': # cuidar de valores nulos
        return 'N/A'

    objeto_data = datetime.strptime(data, '%Y-%m-%d %H:%M:%S') # pega os valores já convertendo para objeto - strp > interpretar

    return objeto_data.strftime('%d/%m/%Y') # retornar formato em string para ptbr - strf > formatar
```

# main

Apresentando Números -  Relatório de Status Manual

```python
import csv # ler arquivos csv

from functions import organizar_texto_categoria, tratar_dimensoes_fisicas, filtro_validação, formatacao_temporal # importando funções que pretendo utilizar

# Contadores para produtos

def executar_pipeline():
    total_produtos = 0
    categorias_corrigidas = 0
    dimensoes_corrigidas = 0

    # Contadores para pedidos
    total_pedidos = 0
    pedidos_sem_aprovacao = 0
    cancelados = 0
    outros_status = 0

    caminho_produtos = "mine_projeto_bloco_1-main/data/raw/olist_products_dataset.csv"
    produtos_sanitizados = []

    caminho_pedidos = "mine_projeto_bloco_1-main/data/raw/olist_orders_dataset.csv"
    pedidos_processados = []
    
    
    # Leitura do arquivo CSV com DictReader
    with open(caminho_produtos, mode='r', encoding='utf-8') as file:

        leitor = csv.DictReader(file)
        
        for linha in leitor:
            total_produtos += 1
            # Aplica a sanitização do texto na coluna de categoria
            categoria_bruta = linha.get('product_category_name')
            if not categoria_bruta or categoria_bruta.strip() == '':
                categorias_corrigidas += 1
            linha['product_category_name'] = organizar_texto_categoria(categoria_bruta)
            
            # Aplica o tratamento das dimensões físicas (peso, altura, etc.)
            linha = tratar_dimensoes_fisicas(linha)
            
            produtos_sanitizados.append(linha)


    with open(caminho_pedidos, mode='r', encoding='utf-8') as file:
        
        leitor = csv.DictReader(file)
        
        for linha in leitor:

            total_pedidos += 1

            data_bruta = linha.get('order_approved_at')
    
            # categoria_bruta = linha.get('product_category_name')

            # Se a categoria original estava vazia, contamos uma correção
            if not data_bruta or data_bruta.strip() == '':
                pedidos_sem_aprovacao += 1
        
            linha['order_approved_at_ptbr'] = formatacao_temporal(data_bruta)
            pedidos_processados.append(linha)

    total_sem_entrega, cancelados, outros_status = filtro_validação(pedidos_processados)
    
    # Apresentação de Dados
    print("=" * 40)
    print("RELATÓRIO DE SANITIZAÇÃO DA BASE OLIST")
    print("=" * 40)
    print(f"Total de produtos processados: {total_produtos}")
    print(f"Categorias nulas tratadas: {categorias_corrigidas}")
    print(f"Total de pedidos processados: {total_pedidos}")
    print(f"Total de pedidos cancelados: {cancelados}")
    print(f"Pedidos sem data de entrega (outros status): {outros_status}")
    print("=" * 40)

executar_pipeline()
```