import csv # ler arquivos csv

from functions import organizar_texto_categoria, tratar_dimensoes_fisicas, formatacao_temporal # importando funções que pretendo utilizar

# Contadores para produtos
total_produtos = 0
categorias_corrigidas = 0
dimensoes_corrigidas = 0

# Contadores para pedidos
total_pedidos = 0
pedidos_sem_aprovacao = 0
cancelados = 0
outros_status = 0



def executar_pipeline():
    caminho_produtos = "mine_projeto_bloco_1-main/data/raw/olist_products_dataset.csv"
    produtos_sanitizados = []

    caminho_pedidos = "mine_projeto_bloco_1-main/data/raw/olist_orders_dataset.csv"
    pedidos_processados = []
    
    
    # 1. Leitura do arquivo CSV com DictReader
    with open(caminho_produtos, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        
        for linha in leitor:
            # Aplica a sanitização do texto na coluna de categoria
            categoria_bruta = linha.get('product_category_name')
            linha['product_category_name'] = organizar_texto_categoria(categoria_bruta)
            
            # Aplica o tratamento das dimensões físicas (peso, altura, etc.)
            linha = tratar_dimensoes_fisicas(linha)
            
            produtos_sanitizados.append(linha)

    with open(caminho_pedidos, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        
        for linha in leitor:
            # 1. Pega o valor da coluna original do CSV
            data_bruta = linha.get('order_approved_at')
            
            # 2. Passa para a função e cria/atualiza o campo com a data formatada
            linha['order_approved_at_ptbr'] = formatacao_temporal(data_bruta)
            
            pedidos_processados.append(linha)
            
    # Exibe o primeiro produto processado para testar
    print("=" * 40)
    print("RELATÓRIO DE SANITIZAÇÃO DA BASE OLIST")
    print("=" * 40)
    print(f"Total de produtos processados: {total_produtos}")
    print(f"Categorias nulas tratadas: {categorias_corrigidas}")
    print(f"Total de pedidos processados: {total_pedidos}")
    print(f"Total de pedidos cancelados: {cancelados}")
    print(f"Pedidos sem data de entrega (outros status): {outros_status}")
    print("=" * 40)
    print(produtos_sanitizados[105])
    print(pedidos_processados[105])

executar_pipeline()