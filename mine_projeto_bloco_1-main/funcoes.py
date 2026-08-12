import re

def sanitizar_texto_categoria(texto): # Padronização de nomes da categoria Produto.
    if not texto or texto.strip() == '':
        return 'sem categoria'

    texto_limpo = texto.lower().strip() # .lower deixa em minúsculas e remove o que não for caracter válido .strip() remove espaços invalidos.

    texto_limpo = re.sub(r'[^a-z0-9_\s]', '', texto_limpo) # re.sub(r'padrão que não sera substituido', 'novo', texto) substitui partes de uma string que correspondem a uma expressão regular

    return texto_limpo

def tratar_dimessoes_fisicas(produto): # Não vou excluir uma linha por completo pederei dados assim, apenas irei definir os valores nulos como 0.0 e converter para float, ou sem categoria.
    campos_dimensoes = [
        'product_category_name', # string(sem categoria)
        'product_weight_g', # float(0.0)
        'product_length_cm', # float(0.0)
        'product_height_cm', # float(0.0)
        'product_width_cm' # float(0.0)
    ]

    for campo in campos_dimensoes:
        valor = produto.get(campo)

        # 1. Se o campo for a categoria de texto
        if campo == 'product_category_name':
            if valor is None or valor.strip() == '':
                produto[campo] = "sem categoria"
            else:
                pass 

        # 2. Se o campo for uma das dimensões numéricas
        else:
            if valor is None or valor.strip() == '':
                produto[campo] = 0.0
            else:
                produto[campo] = float(valor)

    return produto