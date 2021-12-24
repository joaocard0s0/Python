import os 
import shutil
cam = r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\Arquivos_Lojas'
path = os.listdir(cam)

try:
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados')
except:
    pass

try: 
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\RJ')
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\SP')
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\MG')
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\GO')
    os.makedirs(r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\AM')
except:
     pass

try:        
    for i in path:
        if 'RJ' in i:
            print(i)
            shutil.copy2(os.path.join(cam, i), r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\RJ')
        if 'SP' in i:
            shutil.copy2(os.path.join(cam, i), r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\SP')
        if 'MG' in i:
            shutil.copy2(os.path.join(cam, i), r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\MG')
        if 'GO' in i:
            shutil.copy2(os.path.join(cam, i), r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\GO')
        if 'AM' in i:
            shutil.copy2(os.path.join(cam, i), r'D:\ESTUDOS\PYTHON\#Python\21 - ArquivosComputador\estados\AM')
except:
    pass