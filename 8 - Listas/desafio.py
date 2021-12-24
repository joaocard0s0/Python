produtos = ['celular', 'notebook']
estoque = [10, 5]

consultar = input('Qual o produto')

indice = produtos.index(consultar)

print('O estoque do produto {} é:  {}'.format(consultar, estoque[indice]))
