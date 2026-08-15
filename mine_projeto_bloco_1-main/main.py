import csv # ler arquivos csv

<<<<<<< Updated upstream
from functions import organizar_texto_categoria, tratar_dimensoes_fisicas # importando funções que pretendo utilizar
=======
from functions import organizar_texto_categoria, tratar_dimensoes_fisicas, filtro_validação, formatacao_temporal # importando funções que pretendo utilizar

# Contadores para produtos
>>>>>>> Stashed changes

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
    
    # 1. Leitura do arquivo CSV com DictReader
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
<<<<<<< Updated upstream
            
    # Exibe o primeiro produto processado para testar
    print("Exemplo do primeiro produto:")
    print(produtos_sanitizados[105])
=======


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
#    print(produtos_sanitizados[105])
#    print(pedidos_processados[105])

>>>>>>> Stashed changes

executar_pipeline()