lista = [('joao', 21, 60),('lucas', 31, 80), ('rodrigo', 40, 100)]
# Essa estrutura simplifica o for e uma linha
# 1 variavel retorno
# 2 for
peso = [x[2] for x in lista]
peso2 = [(nome, peso) for nome, idade, peso in lista]
maior = max(peso)



filtrando = [(nome, peso) for nome, idade, peso in lista if peso > 80]

print(peso)
print(maior)
print(peso2)
print(filtrando)