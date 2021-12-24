dic = {'nome': 'joao', "idade":21, "peso": 61}


for chave in dic:
    print('{} : {}'.format(chave, dic[chave]))

for x in dic.items():
    print(x)
    