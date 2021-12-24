def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro 
    percentual = (imposto / preco) * 100
    return percentual
    
carga_tributaria(1500, 400, 800)
