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