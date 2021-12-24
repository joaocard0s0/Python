def verificar(validar, par):
    validar = validar.upper()
    par = par.upper()
    if par in validar:
        return True
    else:
        return False
   

names = ['paulo','pedro','cardoso', 'limão', 'carmo', 'joao']

for name in names:
    if verificar(name, "p"):
        print('{} o nome comeca com p '.format(name))