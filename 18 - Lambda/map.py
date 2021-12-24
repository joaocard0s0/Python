def padronizar(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

cod = ['joao ', ' paulo', 'cardoso ']

#for i, ind in enumerate(cod):
 #   cod[i] = padronizar(ind)

cod = list(map(lambda x: padronizar(x), cod))

print(cod)

