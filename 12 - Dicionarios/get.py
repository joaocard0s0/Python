dic = {'nome': 'joao', "idade":21, "peso": 61}
dic2 = {'nome': 'lucas', 'idade': 30, 'peso': 120}

print(dic)
print(dic2)

print('***************PEGAR***************')

nome = dic['nome']
idade = dic.get('idade')

print(nome)
print(idade)

print('***************ATUALIZAR***************')

dic.update({"prof": 'junior'})
dic['nome'] = 'pedro'

print(dic)

print('***************DELETAR***************')

del dic['peso']
print(dic)

dic.clear()
print(dic)
