import pandas as pd

funcionarios = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servico = pd.read_excel('BaseServiçosPrestados.xlsx')
display(funcionarios)
display(clientes)
display(servico)

print('01 ############ ')
soma = funcionarios[['Salario Base', 'Impostos', 'Beneficios', 'VT', 'VR']].sum()
print(soma)
total = soma.sum()
print('o total é {:,.2f}'.format(total))

print('02 ############ ')
servico = servico.merge(clientes, on='ID Cliente')
#display(servico)
servico['temp'] = servico['Valor Contrato Mensal'] * servico['Tempo Total de Contrato (Meses)']
faturamento = servico['temp'].sum()
print("O faturamento foi de {:,}".format(faturamento))

print('03 ############ ')

total_func = len(funcionarios['ID Funcionário'])
func = list(servico['ID Funcionário'])
total_servico = len(set(func))
percentual = (total_servico / total_func) * 100
display(percentual)

# x[coluna].unique()   remove duplicadas mas como sabia transformar em set, fiz desse modo

print('04 ############ ')

new = funcionarios[['ID Funcionário','Area']].merge(servico[['ID Funcionário','Codigo do Servico']], on='ID Funcionário')
display(new)
total_area = new['Area'].value_counts()
print(total_area)

print('05 ############ ')
total = funcionarios['Area'].value_counts()
display(total)


print('06 ############ ')
media = clientes['Valor Contrato Mensal'].mean()
print(media)
