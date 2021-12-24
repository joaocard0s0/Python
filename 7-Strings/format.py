name = 'name here'
cash = 1800

#alinhamento
print('nome {:^50}, show'.format(name))

#colocar valores positivos 
print('nome {:+}, show'.format(cash))

#colocar separador milhar
print('nome {:,}, show'.format(cash))

#colocar casas decimais
print('nome {:,.2f}, show'.format(cash))

#round arredonda
rou = round(cash)
print(rou)