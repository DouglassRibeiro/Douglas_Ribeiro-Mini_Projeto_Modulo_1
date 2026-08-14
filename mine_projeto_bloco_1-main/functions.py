import re

def organizar_texto_categoria(texto): # Padronização de nomes da categoria Produto.
    if not texto or texto.strip() == '':
        return 'sem categoria' # evitando um AttributeError 'product_category_name', já é definido aqui
    
    texto_limpo = texto.lower().strip() # .lower deixa em minúsculas e remove o que não for caracter válido .strip() remove espaços invalidos.

    texto_limpo = re.sub(r'[^a-z0-9_\s]', '', texto_limpo) # re.sub(r'padrão que não sera substituido', 'novo', texto) substitui partes de uma string que correspondem a uma expressão regular

    return texto_limpo

def tratar_dimensoes_fisicas(produto): # Não vou excluir uma linha por completo pederei dados assim, apenas irei definir os valores nulos como 0.0 e converter para float, ou sem categoria.
    campos_dimensoes = [
        #'product_category_name', # string(sem categoria)
       'product_name_lenght', # float 0.0
        'product_description_lenght', # float 0.0
        'product_photos_qty', # float 0.0
        'product_weight_g', # float 0.0
        'product_length_cm', # float 0.0
        'product_height_cm', # float 0.0
        'product_width_cm' # float 0.0
    ]

    for campo in campos_dimensoes:
        valor = produto.get(campo)

        if valor is None or valor.strip() == '':
            produto[campo] = 0.0
        else:
            produto[campo] = float(valor)

    return produto