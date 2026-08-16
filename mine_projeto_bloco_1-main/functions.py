import re
from datetime import datetime

def organizar_texto_categoria(texto): # Padronização de nomes da categoria Produto.
    if not texto or texto.strip() == '':
        return 'sem categoria' # evitando um AttributeError 'product_category_name', já é definido aqui
    
    texto_limpo = texto.lower().strip() # .lower deixa em minúsculas e remove o que não for caracter válido .strip() remove espaços invalidos.

    texto_limpo = re.sub(r'[^a-z0-9_\s]', '', texto_limpo) # re.sub(r'padrão que não sera substituido', 'novo', texto) substitui partes de uma string que correspondem a uma expressão regular

    return texto_limpo

def tratar_dimensoes_fisicas(produto): # Não irei excluir uma linha por completo vou perder dados assim, apenas irei definir os valores nulos como 0.0 e converter todos para float, ou sem categoria.
    campos_dimensoes = [
        #'product_category_name', # string(sem categoria)
        'product_name_lenght', # float(0.0)
        'product_description_lenght', # float(0.0)
        'product_photos_qty', # float(0.0)
        'product_weight_g', # float(0.0)
        'product_length_cm', # float(0.0)
        'product_height_cm', # float(0.0)
        'product_width_cm' # float(0.0)
    ]

    for campo in campos_dimensoes:
        valor = produto.get(campo)

        if valor is None or valor.strip() == '':
            produto[campo] = 0.0
        else:
            produto[campo] = float(valor)

    return produto

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

def formatacao_temporal(data): # %H:%M:%S: Horas, minutos e segundos | %Y: Ano , %m: Mês, %d: Dia

    if not data or data.strip() == '': # cuidar de valores nulos
        return 'N/A'

    objeto_data = datetime.strptime(data, '%Y-%m-%d %H:%M:%S') # pega os valores já convertendo para objeto - strp > interpretar

    return objeto_data.strftime('%d/%m/%Y') # retornar formato em string para ptbr - strf > formatar