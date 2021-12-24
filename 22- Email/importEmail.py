from imap_tools import MailBox, AND 

login = 'your login'
senha = 'your password'

#cada plataforma possui um servidor, esse é do outlook
meu_email = MailBox("imap.gmail.com").login(login, senha)

#pegar email que foram enviados para um remetente específico
#pode colocar as condições .. olhar na biblioteca para ver o que pode usar
#lista = meu_email.fetch(AND(from_="yes-reply@picpay.com",subject='Quer mais DINHEIRO pro Natal?))
lista = meu_email.fetch(AND(from_="joao.jhoni69@gmail.com"))

#print(len(list(lista)))
'''for email in lista:
    print(email.subject)#pega o assunto
    print(email.text)#pega o texto do email
'''

for e in lista:
    if len(e.attachments) > 0:
        for anexo in e.attachments:
            if 'CadastroClientes' in anexo.filename:
                info = anexo.payload
                with open('deucerto.csv', 'wb') as arquivo:
                    arquivo.write(info)
                #wb = escrevendo em byte


