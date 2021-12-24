lista = [100, 200, 300, 500]
item = ['vinho', 'cafeteira', 'microondas', 'iphone']
# filtro simples
imposto = [imp * 0.3 for imp in lista]
print(imposto)

lst = list(zip(lista, item))
lst.sort(reverse=True)
print(lst)

#unpacking
produto = [item for x, item in lst]
print(produto)

