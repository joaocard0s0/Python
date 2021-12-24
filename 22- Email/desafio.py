import win32com.client as win32
import pandas as pd
import os
cam = r'D:\ESTUDOS\PYTHON\#Python\22- Email'
arcs = os.listdir(cam)

path = r'D:\ESTUDOS\PYTHON\#Python\22- Email\Enviar E-mails.xlsx'
read = pd.read_excel(path)


outlook = win32.Dispatch('outlook.application')
                

for i, email in enumerate(read['E-mail']):
    mail = outlook.CreateItem(0)
    mail.to = email
    mail.subject = 'REPORTS'
    mail.body = '''
        Segue-se em anexo os arquivos referente 
        a sua área..

        qualquer dúvida estou à disposição!

        '''
    att = ""
    for arc in arcs:
        if read['Relatório'][i] in arc :
            att = str(cam + f'\\{arc}')
            
    mail.Attachments.Add(att)
    mail.Send()

    





    