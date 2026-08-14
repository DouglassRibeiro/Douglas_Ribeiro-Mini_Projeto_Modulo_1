import csv # ler arquivos csv

from functions import organizar_texto_categoria, tratar_dimensoes_fisicas # importando funções que pretendo utilizar

def executar_pipeline():
    caminho_produtos = "mine_projeto_bloco_1-main/data/raw/olist_products_dataset.csv"
    
    produtos_sanitizados = []
    
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
            
    # Exibe o primeiro produto processado para testar
    print("Exemplo do primeiro produto:")
    print(produtos_sanitizados[105])

executar_pipeline()