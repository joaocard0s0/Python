import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)
print(meses)


plt.plot(meses, vendas, color='green')
plt.axis([0,50, 0, max(vendas)+200])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()


plt.scatter(meses, vendas)
plt.bar(meses, vendas)

plt.figure(1, figsize=(15, 3)) # deve aumentar par conseguir ficar legal
plt.subplot(1, 3, 1) #linhas de graficos, colunas, qual a posicao preenchida agora
plt.plot(meses, vendas, color='green')

plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)

plt.subplot(1, 3, 3)
plt.bar(meses, vendas)
plt.show()