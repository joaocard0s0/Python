import matplotlib.pyplot as plt

venda = [1200, 2000, 5000, 3000]
mes = ['jan', 'fev', 'mar', 'abr']

plt.plot(mes, venda)
plt.ylabel('venda')
plt.xlabel('mes')
plt.axis([0, 12, 0, max(venda)+500])



plt.show()
