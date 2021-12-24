import yagmail
#precisa liberar acesso de apps  menos seguros 
#fica nas conf de acesso do gmail

#logando
usuario = yagmail.SMTP(user='your user', password= 'your password')

#enviando com anexo
usuario.send(to='joao-pongai08@hotmail.com', subject='testando', contents='estou avaliando se esta dando certo', attachments=r'D:\ESTUDOS\PYTHON\Python Impressionador - Hashtag Treinamento\22.Integração Python - E-mail\MATERIAL DE APOIO\Financeiro.xlsx')

#to = para
#subject = Assunto
#Contents = Corpo do texto
#Attachments = path anexo