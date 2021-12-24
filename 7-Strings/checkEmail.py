name = input('nome: ')
email = input('email: ')

if '@' in email and "." in email:
    print('tudo certo')
else:
    print('digite um email valido')