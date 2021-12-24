fsem = [25000,29000,22200,17750,15870,19900]
ssem = [19850,20120,17540,15555,49051,9650]

#extend = coloca uma lista na outra
fsem.extend(ssem)
#sort = colocar em ordem
fsem.sort(reverse=True)


print(fsem)
contador = 0

for x in fsem:
    contador += 1 
    if contador < 4:
        print(f'os maiores valores são: {x}')
    else:
        break


vend = ['lira','joao','diego']
prod = ['ipad', 'iphone']
venda = [
    [100,200],
    [300,500],
    [50,1000],
    [900,10],
]
ipad = venda[1][0]
print(ipad)

total = 0
for x in venda:
    total += x[1]
print(total)