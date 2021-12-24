import win32com.client as win32

#O outlook precisa estar logado em sua conta do pc
#abrir o outlook
outlook = win32.Dispatch('outlook.application')

#escrever o e-mail

mail = outlook.CreateItem(0)
mail.to =  'joao-pongai08@hotmail.com'
mail.Subject = 'TESTANDO OUTLOOK'
mail.Body = '''
Aqui vai o corpo do e-mail
abracos
'''
attachment = r'D:\ESTUDOS\PYTHON\Python Impressionador - Hashtag Treinamento\22.Integração Python - E-mail\MATERIAL DE APOIO\Financeiro.xlsx'
mail.Attachments.Add(attachment)
mail.Send()


