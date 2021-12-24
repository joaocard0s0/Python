lst = ['a ', 'b', 'c ','I'] # sort usa o ascii (ordem definida) olhar no google a tabela
lst.sort()
print(lst)


lst.sort(key=str.casefold) #padroniza a lista
print(lst)

def seg(tupla):
    return tupla[1]

convert = {1: 'a', 2:'I'}
tpl = list(convert.items())
print(tpl)

tpl.sort(key=seg)
print(tpl)


#substitui uma funcao que retorna apenas um valor por uma lamda
def fun(n):
    return n * 2

lambd = lambda n: n * 2
print(lambd(2))


imp = lambda valor: valor * 1.3
print(imp(100))