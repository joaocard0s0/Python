qnt = int(input('Quantas pessoas tem ?? '))
hsp = []

#range percorre determinadamente a quantidade de vezes
for i in range(qnt):
    nome = input('qual o nome: ')
    cpf = input('qual o cpf: ')
    conj = [nome, 'cpf{}'.format(cpf)]
    hsp.append(conj)
print(hsp)
