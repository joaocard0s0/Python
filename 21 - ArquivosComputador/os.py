import os
import shutil

path = r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\Arquivos_Lojas'
caminho = os.listdir(path)


if '201804_Goiania Shopping_GO.csv' in caminho:
    print('Existe')

#criar uma pasta
try:
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\pasta auxiliar')
except:
    pass 
try:
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\pasta auxiliar\new')
except:
    pass
cop = r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\Arquivos_Lojas\201801_Amazonas Shopping_AM.csv'
col = r"D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\pasta auxiliar"
copmove = r"D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\pasta auxiliar\201801_Amazonas Shopping_AM.csv"
mov = r"D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\pasta auxiliar\new\201801_Amazonas Shopping_AM.csv"
try:
    shutil.copy2(cop, col)
except:
    pass
try:
    shutil.move(copmove, mov)
except:
    pass

