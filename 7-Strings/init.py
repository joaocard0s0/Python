name = 'joao'
sobrenome = 'cardoso'
idade = 21
peso = 60

print(len(name))
print(name[0])


#Numeros negativos pegam de tras para frente
print(sobrenome[-1])

#Pegar fracoes do texto
print(sobrenome[1:3])

#format 
print('A idade é de {0} e o peso é de {1}, reforcando a idade é de {0}'.format(idade, peso))

#Primeira letra maiuscula
first = name.capitalize()
print(first)

#todas primeiras maiuscula
total = name + " " +  sobrenome
print(total.title())

#Tudo minusculo
print(first.casefold())

#Saber se o final termina com tais letras
print(sobrenome.endswith('ulo'))

#Saber se o final começa com tais letras
print(sobrenome.startswith('pau'))

#Quantidade de x no texto
print(name.count('o'))

#Econtrar o caracter
print(name.find('j'))

#verfificar se é tudo num, string ou ambos
print(name.isalnum()) #numero + texto
print(name.isnumeric()) #num
print(name.isalpha()) #texto

#Deletar espaços antes e depois dos dados
print(name.strip())

