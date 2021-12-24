from pathlib import Path
import os

#saber em qual pasta esta rodando o cod
print(Path.cwd())
#sempre precisa trocar as \ por /
caminho = Path(r'D:/ESTUDOS/PYTHON/#Python/21 - ArquivosComputador/Arquivos_Lojas')
# listar dados
arquivos = caminho.iterdir()
for arquivo in arquivos:
    print(arquivo) 


#saber se existe algum arquivo
if (caminho / Path('201801_Amazonas Shopping_AM.csv')).exists():
    print('existe')

#criar pasta
Path('pasta').mkdir()
