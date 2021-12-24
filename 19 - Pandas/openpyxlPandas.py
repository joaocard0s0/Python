import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')
#display(tabela)

tabela.loc[tabela['Tipo']=='Serviço', 'Multiplicador Imposto'] = 1.5
tabela['Preço Base Reais'] = tabela['Preço Base Original'] * tabela['Multiplicador Imposto']
display(tabela)

### usando o openpyxl
from openpyxl import workbook, load_workbook

planilha = load_workbook('Produtos.xlsx')
aba_ativa = planilha.active

for tipo in aba_ativa['C']:
    if tipo.value == 'Serviço':
        linha = tipo.row
        aba_ativa[f'D{linha}'] = 1.5
#planilha.save('joaoteste.xlsx')

