cpf = input('DIGITE O CPF')
cpf = cpf.strip()
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('digite o seu cpf corretamente')

