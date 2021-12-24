def funcao(lista, padrao='m'):
    for i, item in enumerate(lista):
        item = item.strip()
        if padrao == 'm':
            item = item.casefold ()
        elif padrao == 'M':
            item = item.upper()
        lista[i] = item
    return lista
    
    

lst = ['aaa ', ' bbb', 'ccc ']

funcao(lst, 'm')
