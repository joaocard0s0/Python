import pandas as pd
#importando os arquivos
vendas_df = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

cliente = clientes_df[['ID Cliente', 'E-mail']]
produto = produtos_df[['ID Produto', 'Nome da Marca']]
loja = lojas_df[['ID Loja', 'Nome da Loja']]


#Unindo todas as tabelas sobre uma coluna !!!

vendas_df = vendas_df.merge(produto, on='ID Produto')
vendas_df = vendas_df.merge(loja, on='ID Loja')
vendas_df = vendas_df.merge(cliente, on='ID Cliente')

vendas_df = vendas_df.rename(columns={'E-mail':'E-mail do Cliente'})

#values_count conta quantos valores possuem iguais
frequencia = vendas_df['E-mail do Cliente'].value_counts()
#figsize ajusta o tamanho a se olhar o a imagem 
#frequencia[:5].plot(figsize=(15, 5))


#loja que mais vendeu
#groupby agrupa valores iguais 
venda_loja = vendas_df.groupby('Nome da Marca').sum()
venda_loja = venda_loja[['Quantidade Vendida']]
venda_loja = venda_loja.sort_values('Quantidade Vendida', ascending=False)

#venda_loja[:5].plot(figsize=(15, 5), kind='bar')

venda_maior = venda_loja['Quantidade Vendida'].max()
melhor_loja = venda_loja['Quantidade Vendida'].idxmax()

#pior loja
venda_pior = venda_loja[-1:]
############################################################

venda_lojac = vendas_df[vendas_df['ID Loja'] == 306]

qnt_vendida = venda_lojac['Quantidade Vendida'].sum()
qnt_devolvida = venda_lojac['Quantidade Devolvida'].sum()
taxa_devolucao = (qnt_devolvida/qnt_vendida)*100

############################################################ Extraindo datas
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')
vendas_df['ano'] = vendas_df['Data da Venda'].dt.year
vendas_df['mes'] = vendas_df['Data da Venda'].dt.month
vendas_df['dia'] = vendas_df['Data da Venda'].dt.day

from tqdm import tqdm #barra de progresso

pbar = tqdm(total=len(vendas_df['ID Loja']), position=0, leave=True)
for i, id_loja in enumerate(vendas_df['ID Loja']):
    pbar.update()
    if id_loja == 222:
        vendas_df.loc[i, 'Quantidade Devolvida'] += 1
display(vendas_df)

