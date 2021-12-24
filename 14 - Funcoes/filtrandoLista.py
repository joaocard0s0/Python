def filtrar(lista, percentual=0.1):
    i = int(percentual * len(lista))
    maiores_lista = lista[i:]
    menores_lista = lista[:i]
    return maiores_lista, menores_lista

lst = [2, 3, 10, 15, 25, 18, 60, 20, 13, 22]    
print(filtrar(lst))   

maiores, menores = filtrar(lst)
print(maiores)
print(menores)